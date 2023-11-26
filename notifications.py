import requests
from PyQt6 import QtCore, QtWidgets
from project import Project, BASE_URL


class Note(Project):
    def __init__(self):
        Project.__init__(self)

        self.proj_id = None
        _translate = QtCore.QCoreApplication.translate
        self._proj_win.setWindowTitle(_translate("Form", "Notifications"))
        self.pushButton.setText(_translate("Form", "Accept"))
        self.pushButton_2.close()

        self.pushButton.clicked.connect(self.accept)

    def render(self):
        self.notes = requests.get(f"{BASE_URL}/list_notes?u_id={self.user_id}").json()
        self.listWidget.clear()
        self.listWidget.addItem(f"title\t Deadline\t\t From \t status ")
        for i in self.notes:
            self.listWidget.addItem(
                f"{i['title']}\t {i['date']} {i['time']}\t {'fr'}\t {'not accepted' if i['status'] == 2 else 'accepted'}")

    def show(self, user_id, proj_id=0):
        self.user_id = user_id
        self.proj_id = proj_id
        self.query = requests.get(f"{BASE_URL}/list_proj_users/{self.proj_id}").json()

        self.fr = requests.get(f"{BASE_URL}/get_name_for_notes/").json()

        self.render()

        self._proj_win.show()

    def accept(self):
        if self.listWidget.currentItem() != None:
            for i in self.notes:
                if self.listWidget.currentItem().text().split('\t')[0] == i['title']:
                    requests.put(f"{BASE_URL}/update_st/?task_id={i['id']}&st={0}").json()
                    self.render()
