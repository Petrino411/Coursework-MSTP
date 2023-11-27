from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
import requests


class Reg(QWidget):
    def __init__(self):
        super().__init__()
        self.pr = []
        self.mw = None
        self.setObjectName("Form")
        self.resize(295, 192)
        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 231, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("current_date_label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.combo = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.combo.setObjectName("combo")
        self.verticalLayout.addWidget(self.combo)

        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.pushButton)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Registration"))
        self.label.setText(_translate("Form", "Registration"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Name"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Register"))

        self.pushButton.clicked.connect(self.register)

        self.render_pr()

    def render_pr(self):
        self.pr = requests.get('http://127.0.0.1:8000/list_projects').json()
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
            q = requests.post('http://127.0.0.1:8000/add_user', json=data).json()

            pr_id = 0
            for i in self.pr:
                if self.combo.currentText() == i['name']:
                    pr_id = i['id']

            data2 = {
                'user_id': q['id'],
                'project_id': pr_id
            }
            requests.post('http://127.0.0.1:8000/user_to_project', json=data2)

            response = requests.get(
                f"http://127.0.0.1:8000/auth?login={str(self.lineEdit.text())}&password={self.lineEdit_2.text()}")
            user_id = int(response.json()['id'])
            from todo import MainWindow
            self.mw = MainWindow(user_id)
            self.mw.show()

            self.close()
            return True


        except:
            print('error')
            return False
