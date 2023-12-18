from PyQt6 import QtCore, QtGui, QtWidgets

import requests
from PyQt6.QtWidgets import QMessageBox

from connection import BASE_URL


class Add:
    def __init__(self):
        self.query = None

        self.proj_id = 0
        self.user_id = 0
        self._winAdd = QtWidgets.QWidget()
        self._winAdd.setWindowIcon(QtGui.QIcon('resources/ico/cat.ico'))
        self._winAdd.resize(328, 365)

        self._winAdd.setFixedSize(328, 365)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self._winAdd.setFont(font)

        self.layoutWidget = QtWidgets.QWidget(parent=self._winAdd)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 308, 341))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QtWidgets.QFormLayout()
        self.date_label = QtWidgets.QLabel(parent=self.layoutWidget)

        self.date_label.setFont(font)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.date_label)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)

        self.dateEdit.setFont(font)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.time_label = QtWidgets.QLabel(parent=self.layoutWidget)

        self.time_label.setFont(font)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.time_label)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.layoutWidget)

        self.timeEdit.setFont(font)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.timeEdit)
        self.title_label = QtWidgets.QLabel(parent=self.layoutWidget)

        self.title_label.setFont(font)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.title_label)
        self.titleLineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)

        self.titleLineEdit.setFont(font)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.titleLineEdit)
        self.desc_label = QtWidgets.QLabel(parent=self.layoutWidget)

        self.desc_label.setFont(font)

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.desc_label)

        self.descEdit = QtWidgets.QTextEdit(parent=self.layoutWidget)

        self.descEdit.setFont(font)

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descEdit)
        self.verticalLayout.addLayout(self.formLayout)

        self.for_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.for_label)

        self.combobox = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.combobox)

        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.pushButton.setFont(font)

        self.verticalLayout.addWidget(self.pushButton)

        _translate = QtCore.QCoreApplication.translate

        self._winAdd.setWindowTitle(_translate("Form", "Добавить"))
        self.date_label.setText(_translate("Form", "Дата:"))
        self.time_label.setText(_translate("Form", "Время:"))
        self.title_label.setText(_translate("Form", "Название:"))
        self.desc_label.setText(_translate("Form", "Описание:"))
        self.for_label.setText(_translate("Form", "Для работника:"))

        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton.clicked.connect(self.execute)

    def execute(self):
        if self.titleLineEdit.text() != '' and self.descEdit.toPlainText() != '':
            u_id = 0
            for i in self.query:
                if self.combobox.currentText() == i['FIO']:
                    u_id = i['id']
            if self.combobox.currentText() == 'Не найдено':
                msg = QMessageBox(self._winAdd)
                msg.setText('Ты не можешь добавить задачу этому пользователю.\n'
                            'Проверь, есть ли у тебя люди в проекте')
                msg.setWindowTitle("Ошибка")
                msg.exec()
            else:
                data = {
                    'date': str(self.dateEdit.date().toPyDate()),
                    'time': str(self.timeEdit.time().currentTime().toPyTime().strftime('%H:%M:%S')),
                    'title': self.titleLineEdit.text(),
                    'description': str(self.descEdit.toPlainText()),
                    'status': 0 if self.user_id == u_id else 2,
                    'user_id': u_id,
                    'project_id': self.proj_id,
                }

                query = requests.post(f'{BASE_URL}/add', json=data)
                if self.user_id != u_id:
                    data2 = {
                        'sender_id': self.user_id,
                        'task_id': query.json()['id'],
                    }
                    requests.post(f'{BASE_URL}/add2', json=data2)

                self.titleLineEdit.clear()
                self.descEdit.clear()
                self._winAdd.close()
        else:
            msg = QMessageBox(self._winAdd)
            msg.setText('Поля не могут быть пустыми')
            msg.setWindowTitle("Ошибка")
            msg.exec()

    def render_users(self):
        self.query = requests.get(f"{BASE_URL}/list_proj_users/{self.proj_id}").json()
        self.combobox.clear()
        if len(self.query) > 0:
            for i in self.query:
                if i['id'] != self.user_id:
                    self.combobox.addItem(i['FIO'])
        else:
            self.combobox.addItem('Не найдено')

    def show(self, date: QtWidgets.QCalendarWidget, user_id, proj_id, permission) -> None:
        self.user_id = user_id
        self.proj_id = proj_id
        self.dateEdit.setDate(date.selectedDate())
        self.timeEdit.setTime(self.timeEdit.time().currentTime())
        self.render_users()
        self._winAdd.show()
