from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox
from back import *
from PyQt6 import QtCore, QtGui, QtWidgets
from add import Add
from edit import Edit
import requests

BASE_URL = 'http://127.0.0.1:8000'

"""Главное окно"""


class MainWindow(QMainWindow):
    def __init__(self, user_id):
        """Интерфейс, сгенерированный с помощью QtDesigner"""
        super().__init__()

        self.user_id = user_id

        self.setObjectName("MainWindow")
        self.resize(631, 610)
        self.setMouseTracking(True)
        self.setFixedSize(self.size())

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 587, 248))
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
        self.widget1.setGeometry(QtCore.QRect(20, 280, 591, 317))
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

        self.current_date_label.setText('Current date: ' + str(self.calendarWidget.selectedDate().toString()))
        self.rmButton.clicked.connect(self.rm_task)
        self.rmButton.clicked.connect(self.renderList)

        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)

        self.listWidget.itemSelectionChanged.connect(self.getDescription)

        self.dateEdit = QtWidgets.QDateEdit()

        self.lst_do = [tuple[str]]
        self.renderList()

        self.msg_add = Add()
        self.msg_add.pushButton.clicked.connect(self.renderList)
        self.msg_edit = Edit()
        self.msg_edit.pushButton.clicked.connect(self.renderList)

        # Data.create__()
        # Data.clear__()
        # db.list_tasks()

    """Отображение выбранной даты"""

    def dateview(self):

        self.current_date_label.setText(f'Current date: {self.calendarWidget.selectedDate().toString()}')

    def renderList(self):
        """Отображение списка дел по дате"""
        self.current_matter_label.setText('Current matter: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = db.get_List_tasks(str(self.calendarWidget.selectedDate().toPyDate()))
        self.lst_do = sorted(self.lst_do)
        for i in range(len(self.lst_do)):
            time = self.lst_do[i][0][:self.lst_do[i][0].rfind(':')]
            self.listWidget.addItem(f'{i + 1}: {time} {self.lst_do[i][1]}\n')
        self.textDescription.clear()
        self.current_matter_label.setText('Current matter: ')

        # self.listWidget.currentIndex()

    def getDescription(self):
        """Отображение описание выбранного дела"""
        text = self.listWidget.currentItem().text()
        index = int(text[:text.find(':')])
        desc = self.lst_do[index - 1][2]
        self.textDescription.setText(str(desc))
        self.current_matter_label.setText(f'Current matter: {str(self.lst_do[index - 1][1])}')

    def add(self):
        """Окно добавления"""
        self.msg_add.show(self.calendarWidget)

    def edit(self):
        """Окно редактирования """
        list = []
        try:
            text = self.listWidget.currentItem().text()
            index = int(text[:text.find(':')])

            list.append(self.calendarWidget.selectedDate())
            list.append(self.lst_do[index - 1])
            self.msg_edit.show(list)
        except(Exception):
            msg = QMessageBox(self)
            msg.setText('Select smth...')
            msg.setWindowTitle("Oh shit")
            msg.exec()

    def rm_task(self):
        if self.listWidget.currentItem() != None:
            text = self.listWidget.currentItem().text()
            index = int(text[:text.find(':')])
            title = self.lst_do[index - 1][1]
            db.remove(title)
            self.renderList()
            self.textDescription.clear()
            self.current_matter_label.setText('Current matter: ')
        else:
            msg = QMessageBox(self)
            msg.setText('Select smth...')
            msg.setWindowTitle("Oh shit")
            msg.exec()
