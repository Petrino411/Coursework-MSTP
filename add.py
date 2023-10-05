from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from back import *




class Add:
    def __init__(self):
        """Интерфейс, сгенерированный с помощью QtDesigner"""
        self._winAdd = QtWidgets.QWidget()
        self._winAdd.setObjectName("Form")
        self._winAdd.resize(328, 365)

        self._winAdd.setFixedSize(328, 365)

        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(9)
        self._winAdd.setFont(font)
        self._winAdd.setStyleSheet("background-color: rgb(23, 33, 43);")
        self.widget = QtWidgets.QWidget(parent=self._winAdd)
        self.widget.setGeometry(QtCore.QRect(10, 10, 308, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.dateLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.dateLabel.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dateLabel)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    " border: 1px solid rgb(35, 46, 60);\n"
                                    "     border-radius:7px;")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.timeLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.timeLabel.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.timeLabel)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    " border: 1px solid rgb(35, 46, 60);\n"
                                    "     border-radius:7px;")
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.timeEdit)
        self.titleLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleLabel.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.titleLineEdit.setFont(font)
        self.titleLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      " border: 1px solid rgb(35, 46, 60);\n"
                                      "     border-radius:7px;")
        self.titleLineEdit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.titleLineEdit)
        self.descLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.descLabel.setFont(font)
        self.descLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.descLabel.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.descLabel)
        self.descEdit = QtWidgets.QTextEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.descEdit.setFont(font)
        self.descEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    " border: 1px solid rgb(35, 46, 60);\n"
                                    "     border-radius:7px;")
        self.descEdit.setObjectName("textEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
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

        QtCore.QMetaObject.connectSlotsByName(self._winAdd)

        _translate = QtCore.QCoreApplication.translate
        self._winAdd.setWindowTitle(_translate("Form", "Add"))
        self.dateLabel.setText(_translate("Form", "Date:"))
        self.timeLabel.setText(_translate("Form", "Time"))
        self.titleLabel.setText(_translate("Form", "Title"))
        self.descLabel.setText(_translate("Form", "Notes:"))
        self.pushButton.setText(_translate("Form", "Add"))

        self.pushButton.clicked.connect(self.execute)


    def execute(self):

        """Кнопка добавить данные в БД"""
        if self.titleLineEdit.text() != '':
            db.add_task(str(self.dateEdit.date().toPyDate()), str(self.timeEdit.time().toPyTime()), str(self.titleLineEdit.text()), str(self.descEdit.toPlainText()))
            self.titleLineEdit.clear()
            self.descEdit.clear()


    def show(self, date: QtWidgets.QCalendarWidget) -> None:
        self.dateEdit.setDate(date.selectedDate())
        self._winAdd.show()






