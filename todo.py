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
    def __init__(self, user_id):

        super().__init__()
        menubar = QMenuBar()

        self.Me = menubar.addMenu('Me')

        self.ch_win = Chat()

        profile = QAction('Profile', self)
        notifications_action = QAction('Notifications', self)
        projects_action = QAction('Projects', self)
        chat_action = QAction('Chat', self)
        exit_action = QAction('Exit', self)

        exit_action.triggered.connect(self.exit)
        chat_action.triggered.connect(self.chat_sh)
        profile.triggered.connect(self.prof_sh)
        projects_action.triggered.connect(self.proj_sh)
        notifications_action.triggered.connect(self.notes_sh)

        self.Me.addAction(profile)
        self.Me.addSeparator()
        self.Me.addAction(notifications_action)
        self.Me.addAction(projects_action)
        self.Me.addSeparator()
        self.Me.addAction(chat_action)
        self.Me.addSeparator()
        self.Me.addAction(exit_action)

        self.setMenuBar(menubar)

        self.user_id = user_id

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
            QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
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
        self.listWidget = QtWidgets.QListWidget(parent=self.widget1)

        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.current_matter_label.setText(_translate("MainWindow", "Current matter:"))
        self.label_5.setText(_translate("MainWindow", "Description:"))
        self.rmButton.setText(_translate("MainWindow", "Remove"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.current_date_label.setText(_translate("MainWindow", "Current date:"))
        self.current_date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setText(_translate("MainWindow", "Plans:"))
        self.current_project_label.setText(_translate("MainWindow", "Project: "))

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

        self.project_combobox.currentTextChanged.connect(self.change_project)

        self.login = Login()



    def dateview(self):
        """Отображение выбранной даты"""
        day = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime("%A")
        date = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime(
            "%d.%m.%Y")
        self.current_date_label.setText(f"{day} {date}")

    def renderList(self):
        """Отображение списка дел по дате"""
        self.current_matter_label.setText('Current matter: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = requests.get(
            f"{BASE_URL}/list_tasks_by_date?date={str(self.calendarWidget.selectedDate().toPyDate())}&user_id={self.user_id}&proj_id={self.selected_proj}").json()
        self.listWidget.addItem(f'№ Time\tTitle\t\t\t\tStatus\n')
        for i in range(len(self.lst_do)):
            time = self.lst_do[i]['time'].split(':')
            if self.lst_do[i]["status"] != 2:
                self.listWidget.addItem(
                    f'{i + 1}:  {time[0]}:{time[1]}\t{self.lst_do[i]["title"]}\t\t{"done" if self.lst_do[i]["status"] == True else "not done"}\n')
        self.textDescription.clear()
        self.current_matter_label.setText('Current matter: ')

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
                title = self.listWidget.currentItem().text().split('\t')[1]
                if self.lst_do[i]['id'] == self.getId(title):
                    self.textDescription.setText(self.lst_do[i]['description'])
            title = str(self.listWidget.currentItem().text().split("\t")[1])
            self.current_matter_label.setText(f'Current matter: {title}') if \
                str(self.listWidget.currentItem().text().split('\t')[
                        1]) != 'Title' else self.current_matter_label.setText(
                'Current matter: ')
        except:
            self.current_matter_label.setText('Current matter: ')

    def add(self):
        """Окно добавления"""
        self.msg_add.show(self.calendarWidget, self.user_id, self.selected_proj)

    def edit(self):
        """Окно редактирования """
        try:
            if self.listWidget.currentItem().text().split('\t')[1] != 'Title':
                task = None

                for i in range(len(self.lst_do)):
                    title = self.listWidget.currentItem().text().split('\t')[1]
                    if self.lst_do[i]['id'] == self.getId(title):
                        task = requests.get(f"{BASE_URL}/list_tasks_by_id/{self.lst_do[i]['id']}").json()
                self.msg_edit.show(self.user_id, task)
        except:
            msg = QMessageBox(self)
            msg.setText('Select smth, idiot')
            msg.setWindowTitle("Oh shit")
            msg.exec()

    def rm_task(self):
        """ Удаление дела"""
        for i in range(len(self.lst_do)):
            title = self.listWidget.currentItem().text().split('\t')[1]
            if self.lst_do[i]['id'] == self.getId(title):
                requests.delete(f"{BASE_URL}/tasks/{self.getId(title)}").json()
                self.renderList()

    def proj_user(self):
        query = requests.get(f"{BASE_URL}/project/{self.user_id}").json()
        if len(query) > 0:
            for i in query:
                self.project_combobox.addItem(i['name'])
            self.selected_proj = query[0]['id']
        else:
            self.project_combobox.addItem('nothing to show')

    def change_project(self):
        query = requests.get(f"{BASE_URL}/project/{self.user_id}").json()
        for i in query:
            if self.project_combobox.currentText() == i['name']:
                self.selected_proj = i['id']
                break
        self.renderList()



    def chat_sh(self):
        self.ch_win.show(self.user_id, self.selected_proj)

    def prof_sh(self):
        query = requests.get(f"{BASE_URL}/profile/{self.user_id}").json()
        self.prof.show(str(query['FIO']), str(query['login']), str(query['password']))


    def proj_sh(self):
        self.proj.show(self.user_id)

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

