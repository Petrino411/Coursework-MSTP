import requests
from PyQt6 import QtCore, QtWidgets
from connection import BASE_URL

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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.fio_label = QtWidgets.QLabel(parent=self.widget)
        self.verticalLayout_2.addWidget(self.fio_label)
        self.login_label = QtWidgets.QLabel(parent=self.widget)
        self.verticalLayout_2.addWidget(self.login_label)
        self.password_label = QtWidgets.QLabel(parent=self.widget)
        self.verticalLayout_2.addWidget(self.password_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.change_button = QtWidgets.QPushButton(parent=self.widget)
        self.horizontalLayout_2.addWidget(self.change_button)
        self.ok_button = QtWidgets.QPushButton(parent=self.widget)
        self.horizontalLayout_2.addWidget(self.ok_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        _translate = QtCore.QCoreApplication.translate
        self._prof_win.setWindowTitle(_translate("Form", "Профиль"))
        self.fio_label.setText(_translate("Form", "ФИО"))
        self.login_label.setText(_translate("Form", "Логин"))
        self.password_label.setText(_translate("Form", "Пароль"))
        self.change_button.setText(_translate("Form", "Изменить"))
        self.ok_button.setText(_translate("Form", "Ок"))

        self.lineEdit_3.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)

        self.change_button.clicked.connect(self.edit)
        self.ok_button.clicked.connect(self.ok)
        self.ok_button.close()

    def edit(self):
        self.lineEdit_3.setDisabled(False)
        self.lineEdit.setDisabled(False)
        self.lineEdit_2.setDisabled(False)
        self.ok_button.show()
        self.change_button.close()

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
        self.change_button.show()
        self.ok_button.close()

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
