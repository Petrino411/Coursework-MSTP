
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from todo import *
import requests

BASE_URL = 'http://127.0.0.1:8000'

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(295, 233)
        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 231, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.loginEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.loginEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.loginEdit)
        self.passEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.passEdit.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.passEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label1 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label1.setObjectName("label")
        self.verticalLayout.addWidget(self.label1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.reg_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.reg_button.setObjectName("label_2")
        self.verticalLayout.addWidget(self.reg_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.label1.setText(_translate("Form", ""))
        self.loginEdit.setText(_translate("Form", "Логин"))
        self.passEdit.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Войти"))
        self.reg_button.setText(_translate("Form", "Зарегистрироваться"))

        self.pushButton.clicked.connect(self.login)

        self.reg_button.clicked.connect(self.reg)
        self.reg_button.setStyleSheet("""
                    QPushButton {
                        border: none;
                    }
                    QPushButton:hover{
	                    background-color: none;
	                    color: rgb(35, 46, 60);
                    }
                """)



    def login(self):
        try:
            response = requests.get(f"{BASE_URL}/auth?login={self.loginEdit.text()}&password={self.passEdit.text()}")
            user_id = int(response.json()['id'])
            self.mw = MainWindow(user_id)
            self.mw.show()
            self.hide()
        except:
            self.label1.setStyleSheet("QLabel{color: rgb(253,44,2);}")
            self.label1.setText('Неверный логин или пароль')

    def reg(self):
        print('sadfg')


