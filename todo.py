from PyQt6.QtWidgets import QMainWindow
from back import *
from PyQt6 import QtCore, QtGui, QtWidgets
from add import Add
from edit import Edit


"""Главное окно"""
class MainWindow(QMainWindow):
    def __init__(self):
        """Интерфейс, сгенерированный с помощью QtDesigner"""
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(631, 610)
        self.setMouseTracking(True)
        self.setFixedSize(self.size())
        self.setStyleSheet("background-color: rgb(23, 33, 43);\n"
                           "color: rgb(226, 226, 226);")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 587, 248))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("background-color: rgb(23, 33, 43);\n"
                                          "alternate-background-color: rgb(35, 46, 60);\n"
                                          "")
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
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.listWidget = QtWidgets.QListWidget(parent=self.widget)
        self.listWidget.setStyleSheet(" border: 1px solid rgb(35, 46, 60);\n"
                                      "     border-radius:7px;")
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
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.textDescription = QtWidgets.QTextBrowser(parent=self.widget1)
        self.textDescription.setStyleSheet(" border: 1px solid rgb(35, 46, 60);\n"
                                       "     border-radius:7px;")
        self.textDescription.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textDescription)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rmButton = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.rmButton.setFont(font)
        self.rmButton.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "     background-color:rgb(24, 37, 51);\n"
                                        "     border: 1px solid rgb(35, 46, 60);\n"
                                        "     border-radius:7px;\n"
                                        "width: 230;\n"
                                        "height: 50;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:rgb(35, 46, 60);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color:rgb(35, 46, 60);\n"
                                        "};")
        self.rmButton.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.rmButton)
        self.editButton = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("QPushButton{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "     background-color:rgb(24, 37, 51);\n"
                                      "     border: 1px solid rgb(35, 46, 60);\n"
                                      "     border-radius:7px;\n"
                                      "width: 230;\n"
                                      "height: 50;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgb(35, 46, 60);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color:rgb(35, 46, 60);\n"
                                      "};")
        self.editButton.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.editButton)
        self.addButton = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton{\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "     background-color:rgb(24, 37, 51);\n"
                                     "     border: 1px solid rgb(35, 46, 60);\n"
                                     "     border-radius:7px;\n"
                                     "width: 230;\n"
                                     "height: 50;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgb(35, 46, 60);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "background-color:rgb(35, 46, 60);\n"
                                     "};")
        self.addButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.addButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.label.setText(_translate("MainWindow", "Current date:"))
        self.label_6.setText(_translate("MainWindow", "Plans:"))
        self.label_2.setText(_translate("MainWindow", "Current matter:"))
        self.label_5.setText(_translate("MainWindow", "Description:"))
        self.rmButton.setText(_translate("MainWindow", "Remove"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.addButton.setText(_translate("MainWindow", "Add"))

        self.calendarWidget.clicked.connect(self.dateview)
        self.calendarWidget.clicked.connect(self.renderList)



        self.label.setText('Current date: ' + str(self.calendarWidget.selectedDate().toString()))
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

        #Data.create__()
        #Data.clear__()
        #db.list_tasks()

    """Отображение выбранной даты"""
    def dateview(self):

        self.label.setText(f'Current date: {self.calendarWidget.selectedDate().toString()}')

    def renderList(self):
        """Отображение списка дел по дате"""
        self.label_2.setText('Current matter: ')
        self.textDescription.clear()
        self.listWidget.clear()
        self.lst_do = db.get_List_tasks(str(self.calendarWidget.selectedDate().toPyDate()))
        self.lst_do = sorted(self.lst_do)
        for i in range(len(self.lst_do)):
            time = self.lst_do[i][0][:self.lst_do[i][0].rfind(':')]
            self.listWidget.addItem(f'{i+1}: {time} {self.lst_do[i][1]}\n')
        self.textDescription.clear()
        self.label_2.setText('Current matter: ')

        #self.listWidget.currentIndex()

    def getDescription(self):
        """Отображение описание выбранного дела"""
        text = self.listWidget.currentItem().text()
        index = int(text[:text.find(':')])
        desc = self.lst_do[index-1][2]
        self.textDescription.setText(str(desc))
        self.label_2.setText(f'Current matter: {str(self.lst_do[index-1][1])}')

    def add(self):
        """Окно добавления"""
        self.msg_add.show(self.calendarWidget)

    def edit(self):
        """Окно редактирования (пока не реализовано)"""
        list = []
        text = self.listWidget.currentItem().text()
        index = int(text[:text.find(':')])
        desc = self.lst_do[index - 1][2]

        list.append(self.calendarWidget.selectedDate())
        list.append(self.lst_do[index-1])
        self.msg_edit.show(list)

    def rm_task(self):
        if self.listWidget.currentItem() != None:
            str = self.listWidget.currentItem().text().split()
            if len(str) == 3:
                title = str[2]
                db.remove(title)
                self.textDescription.clear()
                self.label_2.setText('Current matter: ')


