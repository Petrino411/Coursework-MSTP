import requests
from PyQt6 import QtCore, QtWidgets
BASE_URL = 'http://127.0.0.1:8000'

class Profile:
    def __init__(self):
        super().__init__()
        self.user_id = None
        self.query = None
        self._prof_win = QtWidgets.QWidget()

        self._prof_win.setObjectName("Form")
        self._prof_win.resize(291, 131)
        self.widget = QtWidgets.QWidget(parent=self._prof_win)
        self.widget.setGeometry(QtCore.QRect(50, 10, 193, 109))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("current_date_label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("current_matter_label")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        QtCore.QMetaObject.connectSlotsByName(self._prof_win)

        _translate = QtCore.QCoreApplication.translate
        self._prof_win.setWindowTitle(_translate("Form", "Профиль"))
        self.label.setText(_translate("Form", "ФИО"))
        self.label_2.setText(_translate("Form", "Логин"))
        self.label_3.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Изменить"))
        self.pushButton_2.setText(_translate("Form", "Ок"))

        self.lineEdit_3.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.ok)
        self.pushButton_2.close()

    def edit(self):
        self.lineEdit_3.setDisabled(False)
        self.lineEdit.setDisabled(False)
        self.lineEdit_2.setDisabled(False)
        self.pushButton_2.show()
        self.pushButton.close()

    def ok(self):
        data = {
            'FIO': self.lineEdit_2.text(),
            'login': self.lineEdit.text(),
            'password': self.lineEdit_3.text(),
            'id': self.query['id']
        }
        requests.put(f'{BASE_URL}/update_profile', json=data)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self._prof_win.close()

    def render(self):
        self.query = requests.get(f"{BASE_URL}/profile/{self.user_id}").json()
        fio, login, password = str(self.query['FIO']), str(self.query['login']), str(self.query['password'])
        self.lineEdit_2.setText(fio)
        self.lineEdit.setText(login)
        self.lineEdit_3.setText(password)

    def show(self, user_id):
        self.user_id = user_id
        self.render()
        self._prof_win.show()
