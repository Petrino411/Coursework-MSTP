import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QMessageBox, QApplication

from PyQt6 import QtCore, QtGui, QtWidgets
from add import Add
from edit import Edit
from datetime import datetime
from chat import Chat
from profile import Profile
from project import Project
from notifications import Note

from auth import Login
import requests

BASE_URL = 'http://127.0.0.1:8000'

"""Главное окно"""


class MainWindow(QMainWindow):
    def __init__(self, user_id, permission):
        super().__init__()

        self.task_user = None
        self.user_id = user_id
        self.menubar = QMenuBar()

        self.Me = self.menubar.addMenu('')
        self.set_menu()

        self.ch_win = Chat()

        self.profile = QAction('Профиль', self)
        self.profile.setIcon(QtGui.QIcon('resources/ico/profile.svg'))
        self.notifications_action = QAction('Уведомления', self)
        self.notifications_action.setIcon(QtGui.QIcon('resources/ico/notes.svg'))
        self.projects_action = QAction('Проекты', self)
        self.projects_action.setIcon(QtGui.QIcon('resources/ico/proj.svg'))
        self.chat_action = QAction('Чат', self)
        self.chat_action.setIcon(QtGui.QIcon('resources/ico/chat.svg'))
        self.exit_action = QAction('Выход', self)
        self.exit_action.setIcon(QtGui.QIcon('resources/ico/exit.svg'))
        self.reg_action = QAction('Добавить пользователя', self)
        self.reg_action.setIcon(QtGui.QIcon('resources/ico/add.svg'))

        self.exit_action.triggered.connect(self.exit)
        self.chat_action.triggered.connect(self.chat_sh)
        self.profile.triggered.connect(self.prof_sh)
        self.projects_action.triggered.connect(self.proj_sh)
        self.notifications_action.triggered.connect(self.notes_sh)
        self.reg_action.triggered.connect(self.reg)

        self.Me.addAction(self.profile)
        self.Me.addSeparator()
        self.Me.addAction(self.notifications_action)
        self.Me.addAction(self.projects_action)
        self.Me.addSeparator()
        self.Me.addAction(self.chat_action)
        self.Me.addAction(self.reg_action)
        self.Me.addSeparator()
        self.Me.addAction(self.exit_action)

        self.setMenuBar(self.menubar)

        self.permission = permission

        self.setObjectName("MainWindow")
        self.resize(1040, 576)
        self.setFixedSize(self.size())
        self.setMouseTracking(True)

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 30, 16, 508))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(22, 32, 381, 508))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.calendarWidget.setFont(font)

        self.calendarWidget.setLocale(
            QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.line_2 = QtWidgets.QFrame(parent=self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.current_matter_label = QtWidgets.QLabel(parent=self.widget)

        self.current_matter_label.setFont(font)
        self.current_matter_label.setObjectName("current_matter_label")
        self.verticalLayout.addWidget(self.current_matter_label)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.textDescription = QtWidgets.QTextBrowser(parent=self.widget)

        self.textDescription.setObjectName("textDescription")
        self.verticalLayout.addWidget(self.textDescription)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rmButton = QtWidgets.QPushButton(parent=self.widget)

        self.rmButton.setFont(font)

        self.rmButton.setObjectName("rmButton")
        self.horizontalLayout.addWidget(self.rmButton)
        self.editButton = QtWidgets.QPushButton(parent=self.widget)

        self.editButton.setFont(font)

        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.addButton = QtWidgets.QPushButton(parent=self.widget)

        self.addButton.setFont(font)

        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(427, 30, 591, 511))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.current_date_label = QtWidgets.QLabel(parent=self.widget1)

        self.current_date_label.setFont(font)
        self.current_date_label.setObjectName("current_date_label")

        self.current_project_label = QtWidgets.QLabel(parent=self.widget1)
        self.current_date_label.setFont(font)
        self.current_date_label.setObjectName("current_project_label")

        self.verticalLayout_2.addWidget(self.current_project_label)

        self.project_combobox = QtWidgets.QComboBox(parent=self.widget1)
        self.verticalLayout_2.addWidget(self.project_combobox)

        self.project_combobox.setFixedWidth(200)
        self.project_combobox.setFixedHeight(30)

        self.verticalLayout_2.addWidget(self.current_date_label)
        self.label_6 = QtWidgets.QLabel(parent=self.widget1)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.listWidget = QtWidgets.QTableWidget(parent=self.widget1)
        self.listWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)

        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.listWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.current_matter_label.setText(_translate("MainWindow", "Текущая задача: "))
        self.label_5.setText(_translate("MainWindow", "Описание:"))
        self.rmButton.setText(_translate("MainWindow", "Удалить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.current_date_label.setText(_translate("MainWindow", "Текущая дата: "))
        self.current_date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setText(_translate("MainWindow", "Задачи:"))
        self.current_project_label.setText(_translate("MainWindow", "Проект: "))

        self.selected_proj = 0
        self.proj_user()

        self.calendarWidget.clicked.connect(self.dateview)
        self.calendarWidget.clicked.connect(self.renderList)

        self.dateview()
        self.rmButton.clicked.connect(self.rm_task)
        self.rmButton.clicked.connect(self.renderList)

        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)

        self.listWidget.itemSelectionChanged.connect(self.getDescription)

        self.lst_do = []

        self.renderList()

        self.msg_add = Add()
        self.msg_add.pushButton.clicked.connect(self.renderList)
        self.msg_edit = Edit()
        self.msg_edit.pushButton.clicked.connect(self.renderList)

        self.prof = Profile()

        self.proj = Project()

        self.notes = Note()
        self.notes.pushButton.clicked.connect(self.renderList)

        self.project_combobox.currentTextChanged.connect(self.change_project)

        self.login = Login()
        self.for_permission()

        self.prof.pushButton_2.clicked.connect(self.set_menu)

        self.addButton.setIcon(QtGui.QIcon('resources/ico/add.svg'))
        self.editButton.setIcon(QtGui.QIcon('resources/ico/edit.svg'))
        self.rmButton.setIcon(QtGui.QIcon('resources/ico/delete.svg'))

    def set_menu(self):

        self.Me.setTitle(str(requests.get(f"{BASE_URL}/profile/{self.user_id}").json()['FIO']))

    def for_permission(self):
        if self.permission == 'user':
            self.Me.removeAction(self.reg_action)
            self.addButton.close()
            self.rmButton.close()

    def dateview(self):
        self.calendarWidget.setLocale(
            QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
        """Отображение выбранной даты"""
        day = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime("%A")
        date = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime(
            "%d.%m.%Y")
        self.current_date_label.setText(f"{day} {date}")

    """def renderList(self):
        self.current_matter_label.setText('Текущая задача: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = requests.get(
            f"{BASE_URL}/list_tasks_by_date?date={str(self.calendarWidget.selectedDate().toPyDate())}&proj_id={self.selected_proj}").json()
        if self.permission == 'admin':
            self.listWidget.addItem(f'№ Время\tНазвание\t\tРаботник\t\tСтатус\n') #шапка
        else:
            self.listWidget.addItem(f'№ Время\tНазвание\t\tСтатус\n')
        for i in range(len(self.lst_do)):
            time = self.lst_do[i]['time'].split(':')
            if self.lst_do[i]["status"] != 2 and self.permission == 'user':
                self.listWidget.addItem(
                    f'{i + 1}:  {time[0]}:{time[1]}\t{self.lst_do[i]["title"]}\t\t{"Сделано" if self.lst_do[i]["status"] == True else "На выполнении"}\n')
            elif self.permission == 'admin':
                user = requests.get(f"{BASE_URL}/list_users?user_id={self.lst_do[i]['user_id']}").json()
                self.listWidget.addItem(
                    f'{i + 1}:  {time[0]}:{time[1]}\t{self.lst_do[i]["title"]}\t\t{user['FIO']}\t\t{"Сделано" if self.lst_do[i]["status"] == True else "На выполнении"}\n')
        self.textDescription.clear()
        self.current_matter_label.setText('Текущая задача: ')
        
"""

    def renderList(self):
        self.current_matter_label.setText('Текущая задача: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = requests.get(
            f"{BASE_URL}/list_tasks_by_date?date={str(self.calendarWidget.selectedDate().toPyDate())}&proj_id={self.selected_proj}").json()
        self.listWidget.setRowCount(len(self.lst_do))
        if self.permission == 'admin':
            self.listWidget.setColumnCount(4)
            self.listWidget.setHorizontalHeaderLabels(['Время', 'Название', 'Работник', 'Статус'])  # шапка
        else:
            self.listWidget.setColumnCount(3)
            self.listWidget.setHorizontalHeaderLabels(['Время', 'Название', 'Статус'])
        for row in range(len(self.lst_do)):
            for col in range(self.listWidget.columnCount()):
                time = self.lst_do[row]['time'].split(':')
                if self.lst_do[row]["status"] != 2 and self.permission == 'user' and self.lst_do[row][
                    "user_id"] == self.user_id:
                    item = None
                    if col == 0:
                        item = QtWidgets.QTableWidgetItem(f'{time[0]}:{time[1]}')
                    elif col == 1:
                        item = QtWidgets.QTableWidgetItem(f'{self.lst_do[row]["title"]}')
                    elif col == 2:
                        item = QtWidgets.QTableWidgetItem(
                            f'{"Сделано" if self.lst_do[row]["status"] == True else "На выполнении"}')
                    self.listWidget.setItem(row, col, item)
                elif self.permission == 'admin':
                    item = None
                    user = requests.get(f"{BASE_URL}/list_users?user_id={self.lst_do[row]['user_id']}").json()
                    if col == 0:
                        item = QtWidgets.QTableWidgetItem(f'{time[0]}:{time[1]}')
                    elif col == 1:
                        item = QtWidgets.QTableWidgetItem(f'{self.lst_do[row]["title"]}')
                    elif col == 2:
                        item = QtWidgets.QTableWidgetItem(f'{user['FIO']}')
                    elif col == 3:
                        item = QtWidgets.QTableWidgetItem(
                            f'{"Сделано" if self.lst_do[row]["status"] == True else "На выполнении"}')
                    self.listWidget.setItem(row, col, item)
        self.textDescription.clear()
        self.current_matter_label.setText('Текущая задача: ')

    def getId(self, title):
        """Получение id по названию"""
        for i in range(len(self.lst_do)):
            if self.lst_do[i]['title'] == title:
                return self.lst_do[i]['id']

    def getDescription(self):
        try:
            """Отображение описание выбранного дела"""
            self.current_matter_label.setText('')
            self.textDescription.setText('')

            for i in range(len(self.lst_do)):
                title = self.listWidget.item(self.listWidget.currentRow(), 1).text()
                if self.lst_do[i]['id'] == self.getId(title):
                    self.textDescription.setText(self.lst_do[i]['description'])
            title = str(self.listWidget.item(self.listWidget.currentRow(), 1).text())
            self.current_matter_label.setText(f'Текущая задача: {title}') if \
                self.listWidget.item(self.listWidget.currentRow(), 1).text() != 'Название' \
                else self.current_matter_label.setText('Текущая задача: ')
        except:
            self.current_matter_label.setText('Текущая задача: ')

    def add(self):
        """Окно добавления"""
        self.msg_add.show(self.calendarWidget, self.user_id, self.selected_proj, self.permission)

    def edit(self):
        """Окно редактирования """
        try:
            if self.listWidget.item(self.listWidget.currentRow(), 1).text() != 'Название':
                task = None
                for i in range(len(self.lst_do)):
                    title = self.listWidget.item(self.listWidget.currentRow(), 1).text()
                    if self.lst_do[i]['id'] == self.getId(title):
                        task = requests.get(f"{BASE_URL}/list_tasks_by_id/{self.lst_do[i]['id']}").json()
                self.msg_edit.show(self.user_id, task, self.selected_proj, self.permission)
        except:
            msg = QMessageBox(self)
            msg.setText('Выбери что то')
            msg.setWindowTitle("Ошибка")
            msg.exec()

    def rm_task(self):
        """ Удаление дела"""
        for i in range(len(self.lst_do)):
            title = self.listWidget.item(self.listWidget.currentRow(), 1).text()
            if self.lst_do[i]['id'] == self.getId(title):
                requests.delete(f"{BASE_URL}/tasks/{self.getId(title)}").json()
                self.renderList()

    def proj_user(self):
        query = requests.get(f"{BASE_URL}/project_for_admin").json() if self.permission == 'admin' else requests.get(
            f"{BASE_URL}/project/{self.user_id}").json()
        if len(query) > 0:
            for i in query:
                self.project_combobox.addItem(i['name'])
            self.selected_proj = query[0]['id']
        else:
            self.project_combobox.addItem('Нет работников')

    def change_project(self):
        query = requests.get(f"{BASE_URL}/project_for_admin").json() if self.permission == 'admin' else requests.get(
            f"{BASE_URL}/project/{self.user_id}").json()
        for i in query:
            if self.project_combobox.currentText() == i['name']:
                self.selected_proj = i['id']
                break
        self.renderList()

    def chat_sh(self):
        self.ch_win.show(self.user_id, self.selected_proj)

    def prof_sh(self):
        self.prof.show(self.user_id)

    def proj_sh(self):
        self.proj.show(self.user_id, self.permission)

    def notes_sh(self):
        self.notes.show(self.user_id, self.selected_proj)

    def exit(self):
        self.close()
        self.login.show()

    def closeEvent(self, event):
        for widget in QApplication.topLevelWidgets():
            if widget != self:
                widget.close()

        super().closeEvent(event)

    def reg(self):
        from reg import Reg
        self.reg_win = Reg()
        self.reg_win.show()
