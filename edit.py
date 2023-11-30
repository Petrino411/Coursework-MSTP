import requests.models

from add import *


class Edit(Add):
    def __init__(self):
        super().__init__()
        self.permission = None
        self.task = None
        self.user_id = None

        self.titleFIRST = None
        self.checkBox = QtWidgets.QCheckBox(parent=self.layoutWidget)

        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        _translate = QtCore.QCoreApplication.translate
        self._winAdd.setWindowTitle(_translate("Form", "Изменить"))
        self.pushButton.setText(_translate("Form", "Изменить"))
        self.checkBox.setText(_translate("Form", "Готово"))
        self.label_5.setText(_translate("Form", "Статус"))

    def execute(self):
        if self.permission == "admin":
            if self.titleLineEdit.text() != '':
                u_id = 0
                for i in self.query:
                    if self.combobox.currentText() == i['FIO']:
                        u_id = i['id']
                data = {
                    'date': str(self.dateEdit.date().toPyDate()),
                    'time': str(self.timeEdit.time().toPyTime()),
                    'title': self.titleLineEdit.text(),
                    'description': str(self.descEdit.toPlainText()),
                    'status': 1 if self.checkBox.isChecked() else 0,
                    'user_id': u_id
                }
                if self.user_id != u_id:
                    data2 = {
                        'sender_id': self.user_id,
                        'task_id': self.task["id"],
                    }
                    data['status'] = 2
                    requests.post(f'{BASE_URL}/add2', json=data2)
                requests.put(f'{BASE_URL}/edit/{self.task["id"]}', json=data)

                self._winAdd.close()
                self.titleLineEdit.clear()
                self.descEdit.clear()
        else:
            data = {
                'date': str(self.dateEdit.date().toPyDate()),
                'time': str(self.timeEdit.time().toPyTime()),
                'title': self.titleLineEdit.text(),
                'description': str(self.descEdit.toPlainText()),
                'status': 1 if self.checkBox.isChecked() else 0,
                'user_id': self.user_id
            }
            requests.put(f'{BASE_URL}/edit/{self.task["id"]}', json=data)

    def show(self, user_id, task, proj_id, permission) -> None:
        self.task = task
        self.user_id = user_id
        self.proj_id = proj_id
        self.permission = permission
        if self.permission == 'user':
            self.dateEdit.setDisabled(True)
            self.timeEdit.setDisabled(True)
            self.titleLineEdit.setDisabled(True)
            self.descEdit.setDisabled(True)
            self.combobox.close()
            self.label_for.close()

        date = task['date'].split('-')
        self.dateEdit.setDate(QtCore.QDate(int(date[0]),int(date[1]),int(date[2])))

        self.timeEdit.setTime(QtCore.QTime.fromString(task['time']))
        self.titleLineEdit.setText(task['title'])
#
        self.titleFIRST = task['date']
        self.descEdit.setText(task['description'])
        #self.combobox.close()
        #self.label_for.close()

        self.query = requests.get(f"{BASE_URL}/list_proj_users/{self.proj_id}").json()
        self.combobox.clear()
        if len(self.query) > 0:
            for i in self.query:
                if i['id'] != self.user_id:
                    self.combobox.addItem(i['FIO'])
        else:
            self.combobox.addItem('Не найдено')

        self._winAdd.show()
