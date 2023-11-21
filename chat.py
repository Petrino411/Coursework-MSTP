from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget


class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(411, 320)
        self.textEdit = QtWidgets.QTextEdit(parent=self)
        self.textEdit.setGeometry(QtCore.QRect(10, 270, 331, 41))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.combo = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.combo.setObjectName("combo")
        self.verticalLayout.addWidget(self.combo)
        self.combo.addItem('asfdghj')


        self.listWidget = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setGeometry(QtCore.QRect(360, 280, 31, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Chat"))

