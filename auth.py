from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QLineEdit

import requests

BASE_URL = 'http://127.0.0.1:8000'


class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.mw = None
        self.setObjectName("Auth")
        self.resize(295, 210)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.setFont(font)

        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 231, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("current_date_label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.loginEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.loginEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.loginEdit)
        self.passEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.passEdit.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.passEdit)
        self.loginButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.loginButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.label1 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label1.setObjectName("current_date_label")
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setStyleSheet("QLabel{color: rgb(253,44,2);}")
        self.verticalLayout.addWidget(self.label1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Войти"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.label1.setText(_translate("Form", ""))
        self.loginEdit.setPlaceholderText('Логин')
        self.passEdit.setPlaceholderText('Пароль')
        self.passEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton.setText(_translate("Form", "Войти"))

        self.loginButton.clicked.connect(self.login)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.loginButton.click()
        else:
            super().keyPressEvent(event)

    def login(self):
        if self.loginEdit.text() != '' and self.passEdit.text() != '':
            response = requests.get(
                f"{BASE_URL}/auth?login={str(self.loginEdit.text())}&password={str(self.passEdit.text())}")
            if response.status_code == 404:
                self.label1.setText('Неправильное имя пользователя\nили пароль')
            elif response.status_code == 200:
                user_id = int(response.json()['id'])
                permission = response.json()['root']

                from todo import MainWindow

                self.mw = MainWindow(user_id, permission)
                self.mw.show()
                self.close()
            else:
                self.label1.setText('Что то пошло не так')
        else:
            self.label1.setText('Поля не могут быть пустыми')





