from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
import requests


class Reg(QWidget):
    def __init__(self):
        super().__init__()
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
        self.label.setObjectName("label")
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
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
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

        self.isRegd = None



    def register(self):
        try:
            data = {
                'FIO': self.lineEdit_3.text(),
                'login': str(self.lineEdit.text()),
                'password': self.lineEdit_2.text(),
                'root': "user",
            }
            requests.post('http://127.0.0.1:8000/add_user', json=data)
            self.hide()
            self.isRegd = True

        except:
            print('error')


