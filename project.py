import requests
from PyQt6 import QtCore, QtWidgets

BASE_URL = 'http://127.0.0.1:8000'
class Project:
    def __init__(self):
        self.user_id = 0
        self._proj_win = QtWidgets.QWidget()
        self._proj_win.setObjectName("Form")
        self._proj_win.resize(400, 243)

        #self.widget = QtWidgets.QWidget(parent=self._proj_win)
        #self.widget.setGeometry(QtCore.QRect(10, 10, 381, 225))
        #self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._proj_win)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self._proj_win)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self._proj_win)
        self.pushButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self._proj_win)
        self.pushButton_2.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        QtCore.QMetaObject.connectSlotsByName(self._proj_win)

        _translate = QtCore.QCoreApplication.translate
        self._proj_win.setWindowTitle(_translate("Form", "Projects"))
        self.pushButton.setText(_translate("Form", "Leave"))
        self.pushButton_2.setText(_translate("Form", "Add"))

        self.add_pr = Add_proj()

        self.pushButton_2.clicked.connect(self.add)

    def show(self, user_id):
        self.user_id = user_id
        print('render')
        query = requests.get(f"{BASE_URL}/project/{self.user_id}").json()
        self.listWidget.clear()
        for i in query:
            self.listWidget.addItem(f"{i['name']},  {i['desc']}")
        self._proj_win.show()

    def add(self):
        self.add_pr.show_()



from add import Add
class Add_proj(Add):
    def __init__(self):
        Add.__init__(self)

        self.dateEdit.close()
        self.timeEdit.close()
        self.label.close()
        self.label_2.close()
        self.label_for.close()
        self.combobox.close()

        _translate = QtCore.QCoreApplication.translate

        self._winAdd.setWindowTitle(_translate("Form", "Add project"))

    def show_(self):
        self._winAdd.show()

