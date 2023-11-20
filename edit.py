import requests.models

from add import *


class Edit(Add):
    def __init__(self):
        super().__init__()
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
        self._winAdd.setWindowTitle(_translate("Form", "Edit"))
        self.pushButton.setText(_translate("Form", "Edit"))
        self.checkBox.setText(_translate("Form", "Done"))
        self.label_5.setText(_translate("Form", "Status"))

    def execute(self):
        if self.titleLineEdit.text() != '':
            data = {
                'date': str(self.dateEdit.date().toPyDate()),
                'time': str(self.timeEdit.time().toPyTime()),
                'title': self.titleLineEdit.text(),
                'description': str(self.descEdit.toPlainText()),
                'status': 1 if self.checkBox.isChecked() else 0,
                'user_id': self.user_id
            }
            p = requests.put(f'http://127.0.0.1:8000/edit/{self.task["id"]}', json=data)
            print(self.user_id)
            print(p.json())
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
