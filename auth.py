from PyQt6.QtWidgets import QWidget, QLineEdit
from todo import *
import requests

from reg import Reg

BASE_URL = 'http://127.0.0.1:8000'

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.mw = None
        self.reg_win = Reg()
        self.setObjectName("Auth")
        self.resize(295, 233)
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
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.loginEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.loginEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.loginEdit)
        self.passEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.passEdit.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.passEdit)
        self.loginButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.loginButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.label1 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label1.setObjectName("label")
        self.verticalLayout.addWidget(self.label1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.reg_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.reg_button.setObjectName("label_2")
        self.verticalLayout.addWidget(self.reg_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Auth"))
        self.label.setText(_translate("Form", "Authorization"))
        self.label1.setText(_translate("Form", ""))
        self.loginEdit.setPlaceholderText('Login')
        self.passEdit.setPlaceholderText('Password')
        self.passEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton.setText(_translate("Form", "Sing in"))
        self.reg_button.setText(_translate("Form", "Sign up"))

        self.loginButton.setDefault(True)
        self.loginButton.clicked.connect(self.login)

        self.reg_button.clicked.connect(self.reg)
        self.reg_button.setStyleSheet("""
                    QPushButton {
                        border: none;
                        background-color: rgb(23, 33, 43);
                        color: rgb(27,117,208); 
                        text-decoration: underline;
                    }
                    QPushButton:hover{
	                    
	                    color: rgb(21,92,162);
                    }
                """)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.loginButton.click()
        else:
            super().keyPressEvent(event)



    def login(self):
        #try:
            response = requests.get(f"{BASE_URL}/auth?login={self.loginEdit.text()}&password={self.passEdit.text()}")
            user_id = int(response.json()['id'])
            self.mw = MainWindow(user_id)
            self.mw.show()
            self.hide()
        #rexcept:
        #r    self.label1.setStyleSheet("QLabel{color: rgb(253,44,2);}")
        #r    self.label1.setText('Incorrect username or password.')

    def reg(self):
        #self.hide()
        self.reg_win.show()
        #if self.reg_win.isRegd:
        #    self.reg_win.hide()
        #    response = requests.get(f"{BASE_URL}/auth?login={self.loginEdit.text()}&password={self.passEdit.text()}")
        #    user_id = int(response.json()['id'])
        #    self.mw = MainWindow(user_id)
        #    self.mw.show()




