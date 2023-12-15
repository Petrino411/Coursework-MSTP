from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QLineEdit
import httpx
import asyncio
import requests

from connection import BASE_URL


async def ping_serv(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)
            if response.status_code == 200:
                return 'Сервер в сети'
            else:
                return f"Код ответа:{response.status_code}"
    except httpx.TimeoutException:
        return "Превышено время ожидания"
    except httpx.ConnectError:
        return f"Сервер не в сети"


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    async def run_async(self):
        while True:
            result = await ping_serv(f"{BASE_URL}/connection")
            self.finished.emit(result)
            await asyncio.sleep(2)

    def run(self):
        self.loop.run_until_complete(self.run_async())


class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.mw = None
        self.setObjectName("Auth")
        self.resize(295, 230)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.setFont(font)

        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 231, 201))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.st_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.st_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.loginEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.loginEdit)
        self.passEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.passEdit)
        self.loginButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.loginButton)
        self.error_label = QtWidgets.QLabel(parent=self.layoutWidget)
        font.setPointSize(10)
        self.error_label.setFont(font)
        self.st_label.setFont(font)
        self.error_label.setStyleSheet("QLabel{color: rgb(253,44,2);}")
        self.verticalLayout.addWidget(self.error_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Войти"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.error_label.setText(_translate("Form", ""))
        self.loginEdit.setPlaceholderText('Логин')
        self.passEdit.setPlaceholderText('Пароль')
        self.passEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton.setText(_translate("Form", "Войти"))

        self.loginButton.clicked.connect(self.login)

        self.worker = Worker()
        self.thread = QtCore.QThread(self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.update_st_label)
        self.thread.start()

    def update_st_label(self, result):
        self.st_label.setText(result)
        self.st_label.setStyleSheet(
            "QLabel{color: rgb(0, 207, 0);}") if result == 'Сервер в сети' else self.st_label.setStyleSheet(
            "QLabel{color: rgb(253,44,2);}")

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.loginButton.click()
        else:
            super().keyPressEvent(event)

    def login(self):
        """Авторизация пользователя"""
        if self.st_label.text() != "Сервер в сети":
            return
        if self.loginEdit.text() != '' and self.passEdit.text() != '':
            response = requests.get(
                f"{BASE_URL}/auth?login={str(self.loginEdit.text())}&password={str(self.passEdit.text())}")
            if response.status_code == 404:
                self.error_label.setText('Неправильное имя пользователя\nили пароль')
            elif response.status_code == 200:
                user_id = int(response.json()['id'])
                permission = response.json()['root']

                from todo import MainWindow

                self.mw = MainWindow(user_id, permission)
                self.mw.show()

                self.close()
            else:
                self.error_label.setText('Что-то пошло не так')
        else:
            self.error_label.setText('Поля не могут быть пустыми')
