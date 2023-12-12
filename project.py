import requests
from PyQt6 import QtCore, QtWidgets
from connection import BASE_URL


class Project:
    def __init__(self):
        self.permission = None
        self.user_id = 0
        self._proj_win = QtWidgets.QWidget()
        self._proj_win.resize(400, 243)

        self.verticalLayout = QtWidgets.QVBoxLayout(self._proj_win)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QtWidgets.QListWidget(parent=self._proj_win)
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.pushButton = QtWidgets.QPushButton(parent=self._proj_win)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self._proj_win)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        _translate = QtCore.QCoreApplication.translate
        self._proj_win.setWindowTitle(_translate("Form", "Проекты"))
        self.pushButton.setText(_translate("Form", "Удалить"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))

        self.add_pr = Add_proj()
        self.add_pr.pushButton.clicked.disconnect(self.add_pr.execute)
        self.add_pr.pushButton.clicked.connect(self.render)

        self.pushButton_2.clicked.connect(self.add)

    def render(self):
        query = requests.get(f"{BASE_URL}/project_for_admin").json() if self.permission == 'admin' else requests.get(
            f"{BASE_URL}/project/{self.user_id}").json()
        self.listWidget.clear()
        self.listWidget.addItem(f"Название\t\t\tОписание")
        for i in query:
            self.listWidget.addItem(f"{i['name']}\t\t\t{i['desc']}")

    def show(self, user_id, permission):
        self.permission = permission
        self.user_id = user_id
        self.render()
        self._proj_win.show()

    def add(self):
        self.add_pr.show_()


from add import Add


class Add_proj(Add):
    def __init__(self):
        Add.__init__(self)

        self.dateEdit.close()
        self.timeEdit.close()
        self.date_label.close()
        self.time_label.close()
        self.for_label.close()
        self.combobox.close()

        _translate = QtCore.QCoreApplication.translate

        self._winAdd.setWindowTitle(_translate("Form", "Добавить проект"))
        self.pushButton.clicked.connect(self.add_pr)

    def add_pr(self):
        """ Удаление дела"""
        data = {
            'name': self.titleLineEdit.text(),
            'desc': self.descEdit.toPlainText(),
        }
        requests.post(f'{BASE_URL}/add_project', json=data)
        self._winAdd.close()

    def show_(self):
        self._winAdd.show()
