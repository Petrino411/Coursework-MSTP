import requests.models
from PyQt6.QtWidgets import QDialog

from add import *


class Edit(Add):
    def __init__(self):
        super().__init__()
        self.task = None
        self.user_id = None

        self.titleFIRST = None
        _translate = QtCore.QCoreApplication.translate
        self._winAdd.setWindowTitle(_translate("Form", "Edit"))
        self.pushButton.setText(_translate("Form", "Edit"))

    def execute(self):
        if self.titleLineEdit.text() != '':
            data = {
                'date': str(self.dateEdit.date().toPyDate()),
                'time': str(self.timeEdit.time().toPyTime()),
                'title': self.titleLineEdit.text(),
                'description': str(self.descEdit.toPlainText()),
                'status': 0,
                'user_id': self.user_id
            }
            requests.put(f'http://127.0.0.1:8000/edit/{int(self.task['id'])}', json=data)
            self._winAdd.hide()
            self.titleLineEdit.clear()
            self.descEdit.clear()

    def show(self, user_id, task) -> None:
        self.task = task
        self.user_id = user_id
        date = task['date'].split('-')
        self.dateEdit.setDate(QtCore.QDate(int(date[0]),int(date[1]),int(date[2])))

        self.timeEdit.setTime(QtCore.QTime.fromString(task['time']))
        self.titleLineEdit.setText(task['title'])
#
        self.titleFIRST = task['date']
        self.descEdit.setText(task['description'])
        self._winAdd.show()
