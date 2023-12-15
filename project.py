import requests
from PyQt6 import QtCore, QtWidgets
from connection import BASE_URL


class Project:
    def __init__(self):
        self.permission = None
        self.user_id = 0
        self._proj_win = QtWidgets.QWidget()
        self._proj_win.resize(400, 243)
        self._proj_win.setFixedSize(400, 243)

        self.verticalLayout = QtWidgets.QVBoxLayout(self._proj_win)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QtWidgets.QTableWidget(parent=self._proj_win)
        self.listWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.listWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
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
        self.pushButton.clicked.connect(self.remove_pr)
        self.for_permission()

    def for_permission(self):
        if self.permission != 'admin':
            self.pushButton.close()
            self.pushButton_2.close()

    def render(self):
        query = requests.get(f"{BASE_URL}/project_for_admin").json() if self.permission == 'admin' else requests.get(
            f"{BASE_URL}/project/{self.user_id}").json()
        self.listWidget.clear()
        self.listWidget.setColumnCount(2)
        self.listWidget.setHorizontalHeaderLabels(['Название', 'Описание'])
        self.listWidget.setRowCount(len(query))
        for row in range(len(query)):
            for col in range(self.listWidget.columnCount()):
                item = None
                if col == 0:
                    item = QtWidgets.QTableWidgetItem(f'{query[row]['name']}')
                elif col == 1:
                    item = QtWidgets.QTableWidgetItem(f'{query[row]['desc']}')
                self.listWidget.setItem(row, col, item)

    def show(self, user_id, permission):
        self.permission = permission
        self.user_id = user_id
        self.render()
        self._proj_win.show()

    def add(self):
        self.add_pr.show_()

    def remove_pr(self):
        title = self.listWidget.item(self.listWidget.currentRow(), 0).text()
        requests.delete(f"{BASE_URL}/project/{title}").json()
        self.render()



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
