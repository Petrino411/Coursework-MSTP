from PyQt6 import QtCore, QtGui, QtWidgets

import requests


BASE_URL = 'http://127.0.0.1:8000/add'

class Add:
    def __init__(self):
        self.user_id = None
        self._winAdd = QtWidgets.QWidget()
        self._winAdd.setObjectName("Form")
        self._winAdd.resize(328, 365)

        self._winAdd.setFixedSize(328, 365)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self._winAdd.setFont(font)

        self.layoutWidget = QtWidgets.QWidget(parent=self._winAdd)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 308, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)

        self.label.setFont(font)

        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)

        self.dateEdit.setFont(font)

        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)

        self.label_2.setFont(font)

        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.layoutWidget)

        self.timeEdit.setFont(font)

        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.timeEdit)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)

        self.label_4.setFont(font)

        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.titleLineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)

        self.titleLineEdit.setFont(font)

        self.titleLineEdit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.titleLineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)

        self.label_3.setFont(font)

        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)

        self.descEdit = QtWidgets.QTextEdit(parent=self.layoutWidget)

        self.descEdit.setFont(font)

        self.descEdit.setObjectName("textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.pushButton.setFont(font)

        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)


        QtCore.QMetaObject.connectSlotsByName(self._winAdd)


        _translate = QtCore.QCoreApplication.translate

        self._winAdd.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Date:"))
        self.label_2.setText(_translate("Form", "Time"))
        self.label_4.setText(_translate("Form", "Title"))
        self.label_3.setText(_translate("Form", "Notes:"))

        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton.clicked.connect(self.execute)


    def execute(self):
        """Кнопка добавить данные в БД"""
        print(self.descEdit.toPlainText())
        if self.titleLineEdit.text() != '':
            data = {
                'date': str(self.dateEdit.date().toPyDate()),
                'time': str(self.timeEdit.time().currentTime().toPyTime().strftime('%H:%M:%S')),
                'title': self.titleLineEdit.text(),
                'description': str(self.descEdit.toPlainText()),
                'status': 0,
                'user_id': self.user_id
            }
            requests.post('http://127.0.0.1:8000/add', json=data)
            self.titleLineEdit.clear()
            self.descEdit.clear()
            self._winAdd.hide()

    def show(self, date: QtWidgets.QCalendarWidget, user_id) -> None:
        self.user_id = user_id
        self.dateEdit.setDate(date.selectedDate())
        self.timeEdit.setTime(self.timeEdit.time().currentTime())
        self._winAdd.show()
