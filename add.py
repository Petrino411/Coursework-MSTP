from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Add(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(351, 300)
        self.setFixedSize(self.size())
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(9)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(23, 33, 43);")
        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 294, 275))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    " border: 1px solid rgb(35, 46, 60);\n"
                                    "     border-radius:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    " border: 1px solid rgb(35, 46, 60);\n"
                                    "     border-radius:7px;")
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    " border: 1px solid rgb(35, 46, 60);\n"
                                    "     border-radius:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "     background-color:rgb(24, 37, 51);\n"
                                        "     border: 1px solid rgb(35, 46, 60);\n"
                                        "     border-radius:7px;\n"
                                        "width: 230;\n"
                                        "height: 50;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:rgb(35, 46, 60);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color:rgb(35, 46, 60);\n"
                                        "};")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Add"))
        self.label.setText(_translate("Form", "Date:"))
        self.label_2.setText(_translate("Form", "Title:"))
        self.label_3.setText(_translate("Form", "Notes:"))
        self.pushButton.setText(_translate("Form", "Add"))
