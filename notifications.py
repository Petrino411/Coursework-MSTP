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
        self.pushButton.clicked.disconnect(self.remove_pr)
        self.pushButton.clicked.connect(self.accept)

    def render(self):
        self.notes = requests.get(f"{BASE_URL}/list_notes?u_id={self.user_id}").json()
        self.listWidget.clear()
        self.listWidget.setColumnCount(4)
        self.listWidget.setHorizontalHeaderLabels(['Название', 'Дедлайн', 'От', 'Статус'])
        self.listWidget.setRowCount(len(self.notes))
        for row in range(len(self.notes)):
            for col in range(self.listWidget.columnCount()):
                item = None
                if col == 0:
                    item = QtWidgets.QTableWidgetItem(f'{self.notes[row]['title']}')
                elif col == 1:
                    item = QtWidgets.QTableWidgetItem(f'{self.notes[row]['date']}')
                elif col == 2:
                    item = QtWidgets.QTableWidgetItem(f'{requests.get(f"{BASE_URL}/get_name_for_notes?task_id={self.notes[row]['id']}").json()}')
                elif col == 3:
                    item = QtWidgets.QTableWidgetItem(f'{'Не принято' if self.notes[row]['status'] == 2 else 'Принятно'}')
                self.listWidget.setItem(row, col, item)

    def show(self, user_id, proj_id=0):
        self.user_id = user_id
        self.proj_id = proj_id
        self.query = requests.get(f"{BASE_URL}/list_proj_users/{self.proj_id}").json()

        self.fr = requests.get(f"{BASE_URL}/get_name_for_notes/").json()
        self.render()

        self._proj_win.show()

    def accept(self):
        if self.listWidget.item(self.listWidget.currentRow(), 0).text() != 'Название':
            for i in self.notes:
                if self.listWidget.item(self.listWidget.currentRow(), 0).text() == i['title']:
                    requests.put(f"{BASE_URL}/update_st/?task_id={i['id']}&st={0}").json()
                    self.render()
