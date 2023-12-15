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

from connection import BASE_URL


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self, user_id, permission):
        super().__init__()

        self.user_id = user_id
        self.permission = permission
        self.task_user = None
        self.selected_proj = 0
        self.lst_do = []
        self.menubar = QMenuBar()

        self.Me = self.menubar.addMenu('')
        self.set_menu()

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

        self.setObjectName("MainWindow")
        self.resize(1040, 576)
        self.setFixedSize(self.size())
        self.setMouseTracking(True)

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 30, 16, 508))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(22, 32, 381, 508))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.calendarWidget.setFont(font)

        self.calendarWidget.setLocale(
            QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
        self.verticalLayout.addWidget(self.calendarWidget)
        self.line_2 = QtWidgets.QFrame(parent=self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.verticalLayout.addWidget(self.line_2)
        self.current_matter_label = QtWidgets.QLabel(parent=self.widget)

        self.current_matter_label.setFont(font)
        self.verticalLayout.addWidget(self.current_matter_label)
        self.desc_label = QtWidgets.QLabel(parent=self.widget)

        self.desc_label.setFont(font)
        self.verticalLayout.addWidget(self.desc_label)
        self.textDescription = QtWidgets.QTextBrowser(parent=self.widget)
        self.textDescription.setFont(font)

        self.verticalLayout.addWidget(self.textDescription)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.rmButton = QtWidgets.QPushButton(parent=self.widget)

        self.rmButton.setFont(font)

        self.horizontalLayout.addWidget(self.rmButton)
        self.editButton = QtWidgets.QPushButton(parent=self.widget)

        self.editButton.setFont(font)

        self.horizontalLayout.addWidget(self.editButton)
        self.addButton = QtWidgets.QPushButton(parent=self.widget)

        self.addButton.setFont(font)

        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(427, 30, 591, 511))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.current_date_label = QtWidgets.QLabel(parent=self.widget1)

        self.current_date_label.setFont(font)

        self.current_project_label = QtWidgets.QLabel(parent=self.widget1)
        self.current_date_label.setFont(font)

        self.verticalLayout_2.addWidget(self.current_project_label)

        self.project_combobox = QtWidgets.QComboBox(parent=self.widget1)
        self.verticalLayout_2.addWidget(self.project_combobox)

        self.project_combobox.setFixedWidth(200)
        self.project_combobox.setFixedHeight(30)

        self.verticalLayout_2.addWidget(self.current_date_label)
        self.tasks_label = QtWidgets.QLabel(parent=self.widget1)

        self.tasks_label.setFont(font)
        self.verticalLayout_2.addWidget(self.tasks_label)
        self.listWidget = QtWidgets.QTableWidget(parent=self.widget1)
        self.listWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.listWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Система управления задачами и проектами"))
        self.current_matter_label.setText(_translate("MainWindow", "Текущая задача: "))
        self.desc_label.setText(_translate("MainWindow", "Описание:"))
        self.rmButton.setText(_translate("MainWindow", "Удалить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.current_date_label.setText(_translate("MainWindow", "Текущая дата: "))
        self.current_date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tasks_label.setText(_translate("MainWindow", "Задачи:"))
        self.current_project_label.setText(_translate("MainWindow", "Проект: "))

        self.proj_user()
        self.dateview()
        self.renderList()
        self.for_permission()

        self.proj = Project()
        self.prof = Profile()
        self.msg_edit = Edit()
        self.msg_add = Add()
        self.notes = Note()
        self.login = Login()
        self.ch_win = Chat()

        self.calendarWidget.clicked.connect(self.dateview)
        self.calendarWidget.clicked.connect(self.renderList)
        self.rmButton.clicked.connect(self.rm_task)
        self.rmButton.clicked.connect(self.renderList)
        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.listWidget.itemSelectionChanged.connect(self.getDescription)
        self.msg_add.pushButton.clicked.connect(self.renderList)
        self.msg_edit.pushButton.clicked.connect(self.renderList)
        self.proj.pushButton.clicked.connect(self.proj_user)
        self.proj.add_pr.pushButton.clicked.connect(self.proj_user)
        self.notes.pushButton.clicked.connect(self.renderList)
        self.project_combobox.currentTextChanged.connect(self.change_project)
        self.prof.ok_button.clicked.connect(self.set_menu)

        self.addButton.setIcon(QtGui.QIcon('resources/ico/add.svg'))
        self.editButton.setIcon(QtGui.QIcon('resources/ico/edit.svg'))
        self.rmButton.setIcon(QtGui.QIcon('resources/ico/delete.svg'))

    def set_menu(self):
        """Меню пользователя"""
        self.Me.setTitle(str(requests.get(f"{BASE_URL}/profile/{self.user_id}").json()['FIO']))

    def for_permission(self):
        """Проверка разрешений пользователя"""
        if self.permission == 'user':
            self.Me.removeAction(self.reg_action)
            self.addButton.close()
            self.rmButton.close()
        else:
            self.Me.removeAction(self.notifications_action)

    def dateview(self):
        """Отображение выбранной даты"""
        self.calendarWidget.setLocale(
            QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
        day = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime("%A")
        date = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime(
            "%d.%m.%Y")
        self.current_date_label.setText(f"{day} {date}")

    def renderList(self):
        """Запрос и парсинг списка дел по дате из БД"""
        self.current_matter_label.setText('Текущая задача: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = requests.get(
            f"{BASE_URL}/list_tasks_by_date?date={str(self.calendarWidget.selectedDate().toPyDate())}&proj_id={self.selected_proj}").json()
        self.listWidget.setRowCount(len(self.lst_do))
        if self.permission == 'admin':
            self.listWidget.setColumnCount(4)
            self.listWidget.setHorizontalHeaderLabels(['Время', 'Название', 'Работник', 'Статус'])
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
        """Отображение описание выбранного дела"""
        try:
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
        """Проекты пользователя"""
        self.project_combobox.clear()
        query = requests.get(f"{BASE_URL}/project_for_admin").json() if self.permission == 'admin' else requests.get(
            f"{BASE_URL}/project/{self.user_id}").json()
        if len(query) > 0:
            for i in query:
                self.project_combobox.addItem(i['name'])
            self.selected_proj = query[0]['id']
        else:
            self.project_combobox.addItem('Нет проектов')

    def change_project(self):
        """Смена проекта"""
        query = requests.get(f"{BASE_URL}/project_for_admin").json() if self.permission == 'admin' else requests.get(
            f"{BASE_URL}/project/{self.user_id}").json()
        for i in query:
            if self.project_combobox.currentText() == i['name']:
                self.selected_proj = i['id']
                break
        self.renderList()

    def chat_sh(self):
        """Показ чата"""
        self.ch_win.show(self.user_id, self.selected_proj)

    def prof_sh(self):
        """Показ профиля"""
        self.prof.show(self.user_id)

    def proj_sh(self):
        """Показ проектов"""
        self.proj.show(self.user_id, self.permission)

    def notes_sh(self):
        """Показ уцвведомлений"""
        self.notes.show(self.user_id, self.selected_proj)

    def exit(self):
        """Выход пользователя"""
        self.close()
        self.login.show()

    def closeEvent(self, event):
        for widget in QApplication.topLevelWidgets():
            if widget != self:
                widget.close()

        super().closeEvent(event)

    def reg(self):
        """Показ регистрации"""
        from reg import Reg
        self.reg_win = Reg()
        self.reg_win.show()
