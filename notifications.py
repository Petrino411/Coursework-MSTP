import requests
from PyQt6 import QtCore, QtWidgets
from project import Project
from connection import BASE_URL


class Note(Project):
    def __init__(self):
        Project.__init__(self)

        self.notes = None
        self.query = None
        self.proj_id = None
        _translate = QtCore.QCoreApplication.translate
        self._proj_win.setWindowTitle(_translate("Form", "Уведомления"))
        self.pushButton.setText(_translate("Form", "Принять"))
        self.pushButton_2.close()

        self.pushButton.clicked.connect(self.accept)

    def render(self):
        self.notes = requests.get(f"{BASE_URL}/list_notes?u_id={self.user_id}").json()
        self.listWidget.clear()
        self.listWidget.addItem(f"Название\t Дедлайн\t\t От \t Статус ")
        for i in self.notes:
            self.listWidget.addItem(
                f"{i['title']}\t {i['date']} {i['time']}\t {requests.get(f"{BASE_URL}/get_name_for_notes?task_id={i['id']}").json()}\t {'Не принято' if i['status'] == 2 else 'Принятно'}")

    def show(self, user_id, proj_id=0):
        self.user_id = user_id
        self.proj_id = proj_id
        self.query = requests.get(f"{BASE_URL}/list_proj_users/{self.proj_id}").json()

        self.fr = requests.get(f"{BASE_URL}/get_name_for_notes/").json()

        self.render()

        self._proj_win.show()

    def accept(self):
        if self.listWidget.currentItem() is not None:
            for i in self.notes:
                if self.listWidget.currentItem().text().split('\t')[0] == i['title']:
                    requests.put(f"{BASE_URL}/update_st/?task_id={i['id']}&st={0}").json()
                    self.render()
