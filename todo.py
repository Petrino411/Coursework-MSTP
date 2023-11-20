from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QMenuBar

from PyQt6 import QtCore, QtGui, QtWidgets
from add import Add
from edit import Edit
from datetime import datetime

import requests

BASE_URL = 'http://127.0.0.1:8000'

"""Главное окно"""


class MainWindow(QMainWindow):
    def __init__(self, user_id):

        super().__init__()
        menubar = QMenuBar()

        self.file_menu = menubar.addMenu('Me')


        notifications_action = QAction('Notifications', self)
        projects_action = QAction('Projects', self)
        self.file_menu.addAction(notifications_action)
        self.file_menu.addAction(projects_action)

        self.setMenuBar(menubar)

        self.user_id = user_id

        self.setObjectName("MainWindow")
        self.resize(670, 630)
        self.setMouseTracking(True)
        self.setFixedSize(self.size())

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 630, 248))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.widget)

        self.calendarWidget.setFont(font)

        self.calendarWidget.setLocale(
            QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_3.addWidget(self.calendarWidget)
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.current_date_label = QtWidgets.QLabel(parent=self.widget)
        self.current_date_label.setFont(font)
        self.current_date_label.setObjectName("label")
        self.horizontalLayout.addWidget(self.current_date_label)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Plans_label = QtWidgets.QLabel(parent=self.widget)
        self.Plans_label.setFont(font)
        self.Plans_label.setObjectName("label_6")
        self.verticalLayout.addWidget(self.Plans_label)
        self.listWidget = QtWidgets.QListWidget(parent=self.widget)

        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)



        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 280, 630, 317))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(parent=self.widget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.current_matter_label = QtWidgets.QLabel(parent=self.widget1)
        self.current_matter_label.setFont(font)
        self.current_matter_label.setObjectName("label_2")
        self.current_date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2.addWidget(self.current_matter_label)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.desc_label = QtWidgets.QLabel(parent=self.widget1)
        self.desc_label.setFont(font)
        self.desc_label.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.desc_label)
        self.textDescription = QtWidgets.QTextBrowser(parent=self.widget1)

        self.textDescription.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textDescription)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rmButton = QtWidgets.QPushButton(parent=self.widget1)
        self.rmButton.setFont(font)
        self.rmButton.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.rmButton)
        self.editButton = QtWidgets.QPushButton(parent=self.widget1)
        self.editButton.setFont(font)
        self.editButton.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.editButton)
        self.addButton = QtWidgets.QPushButton(parent=self.widget1)
        self.addButton.setFont(font)
        self.addButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.addButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.current_date_label.setText(_translate("MainWindow", "Current date:"))
        self.Plans_label.setText(_translate("MainWindow", "Plans:"))
        self.current_matter_label.setText(_translate("MainWindow", "Current matter:"))
        self.desc_label.setText(_translate("MainWindow", "Description:"))
        self.rmButton.setText(_translate("MainWindow", "Remove"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.addButton.setText(_translate("MainWindow", "Add"))

        self.calendarWidget.clicked.connect(self.dateview)
        self.calendarWidget.clicked.connect(self.renderList)

        self.dateview()
        self.rmButton.clicked.connect(self.rm_task)
        self.rmButton.clicked.connect(self.renderList)

        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)

        self.listWidget.itemSelectionChanged.connect(self.getDescription)

        self.dateEdit = QtWidgets.QDateEdit()

        self.lst_do = []
        self.renderList()

        self.msg_add = Add()
        self.msg_add.pushButton.clicked.connect(self.renderList)
        self.msg_edit = Edit()
        self.msg_edit.pushButton.clicked.connect(self.renderList)


        # Data.create__()
        # Data.clear__()
        # db.list_tasks()

    """Отображение выбранной даты"""


    def for_datewiev(self):
        day = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime("%A")
        date = datetime.strptime(str(self.calendarWidget.selectedDate().toPyDate()), '%Y-%m-%d').date().strftime("%d.%m.%Y")
        return f"{day} {date}"

    def dateview(self):
        self.current_date_label.setText(self.for_datewiev())

    def renderList(self):
        """Отображение списка дел по дате"""
        self.current_matter_label.setText('Current matter: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = requests.get(f"{BASE_URL}/list_tasks_by_date?date={str(self.calendarWidget.selectedDate().toPyDate())}&user_id={self.user_id}").json()
        self.listWidget.addItem(f'№ Time\tTitle\t\tStatus\n')
        for i in range(len(self.lst_do)):
            time = self.lst_do[i]['time'].split(':')
            self.listWidget.addItem(f'{i+1}:  {time[0]}:{time[1]}\t{self.lst_do[i]["title"]}\t\t{"done" if self.lst_do[i]["status"] == True else "not done"}\n')
        self.textDescription.clear()
        self.current_matter_label.setText('Current matter: ')

    def getId(self, title):
        for i in range(len(self.lst_do)):
            if self.lst_do[i]['title'] == title:
                return self.lst_do[i]['id']


    def getDescription(self):
        self.current_matter_label.setText('')
        self.textDescription.setText('')
        """Отображение описание выбранного дела"""
        for i in range(len(self.lst_do)):
            title = self.listWidget.currentItem().text().split('\t')[1]
            if self.lst_do[i]['id'] == self.getId(title):
                self.textDescription.setText(self.lst_do[i]['description'])
        titile = str(self.listWidget.currentItem().text().split("\t")[1])
        self.current_matter_label.setText(f'Current matter: {titile}') if\
            str(self.listWidget.currentItem().text().split('\t')[1]) != 'Title' else self.current_matter_label.setText('Current matter: ')

    def add(self):
        """Окно добавления"""
        self.msg_add.show(self.calendarWidget, self.user_id)


    def edit(self):
        if self.listWidget.currentItem().text().split('\t')[1] != 'Title':
            task = None
            """Окно редактирования """
            for i in range(len(self.lst_do)):
                title = self.listWidget.currentItem().text().split('\t')[1]
                if self.lst_do[i]['id'] == self.getId(title):
                    task = requests.get(f"{BASE_URL}/list_tasks_by_id/{self.lst_do[i]['id']}").json()
            self.msg_edit.show(self.user_id,task)

    def rm_task(self):
        for i in range(len(self.lst_do)):
            title = self.listWidget.currentItem().text().split('\t')[1]
            if self.lst_do[i]['id'] == self.getId(title):
                requests.delete(f"{BASE_URL}/tasks/{self.getId(title)}").json()
                self.renderList()



