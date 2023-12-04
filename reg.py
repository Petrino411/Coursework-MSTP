from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
import requests

from connection import BASE_URL

class Reg(QWidget):
    def __init__(self):
        super().__init__()
        self.pr = []
        self.mw = None
        self.resize(295, 192)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(parent=self)
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self)
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.combo = QtWidgets.QComboBox(parent=self)
        self.verticalLayout.addWidget(self.combo)

        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.verticalLayout.addWidget(self.pushButton)
        self.combo.setFixedHeight(30)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "ФИО"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Регистрация"))

        self.pushButton.clicked.connect(self.register)

        self.render_pr()

    def render_pr(self):
        self.pr = requests.get(f'{BASE_URL}/list_projects').json()
        for i in self.pr:
            self.combo.addItem(str(i['name']))

    def register(self) -> bool:
        try:
            data = {
                'FIO': self.lineEdit_3.text(),
                'login': str(self.lineEdit.text()),
                'password': self.lineEdit_2.text(),
                'root': "user",
            }
            q = requests.post(f'{BASE_URL}/add_user', json=data).json()

            pr_id = 0
            for i in self.pr:
                if self.combo.currentText() == i['name']:
                    pr_id = i['id']

            data2 = {
                'user_id': q['id'],
                'project_id': pr_id
            }
            requests.post(f'{BASE_URL}/user_to_project', json=data2)

            self.close()
            return True


        except:
            print('error')
            return False
