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
        self.reg_label = QtWidgets.QLabel(parent=self)
        self.verticalLayout.addWidget(self.reg_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.fio_label = QtWidgets.QLineEdit(parent=self)
        self.verticalLayout.addWidget(self.fio_label)
        self.login_edit = QtWidgets.QLineEdit(parent=self)
        self.verticalLayout.addWidget(self.login_edit)
        self.password_edit = QtWidgets.QLineEdit(parent=self)
        self.verticalLayout.addWidget(self.password_edit)
        self.combo = QtWidgets.QComboBox(parent=self)
        self.verticalLayout.addWidget(self.combo)

        self.reg_button = QtWidgets.QPushButton(parent=self)
        self.verticalLayout.addWidget(self.reg_button)
        self.combo.setFixedHeight(30)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Регистрация"))
        self.reg_label.setText(_translate("Form", "Регистрация"))
        self.fio_label.setPlaceholderText(_translate("Form", "ФИО"))
        self.login_edit.setPlaceholderText(_translate("Form", "Логин"))
        self.password_edit.setPlaceholderText(_translate("Form", "Пароль"))
        self.reg_button.setText(_translate("Form", "Регистрация"))

        self.reg_button.clicked.connect(self.register)

        self.render_pr()

    def render_pr(self):
        self.pr = requests.get(f'{BASE_URL}/list_projects').json()
        for i in self.pr:
            self.combo.addItem(str(i['name']))

    def register(self) -> bool:
        try:
            data = {
                'FIO': self.fio_label.text(),
                'login': str(self.login_edit.text()),
                'password': self.password_edit.text(),
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
