from datetime import datetime

import requests
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

BASE_URL = 'http://127.0.0.1:8000'

class Chat:
    def __init__(self):
        self.sort_hist = []
        self.user_id = 0
        self.query = []
        self.proj_id = 0
        self._winAdd = QtWidgets.QWidget()
        self._winAdd.setObjectName("Form")
        self._winAdd.resize(411, 320)
        self.textEdit = QtWidgets.QTextEdit(parent=self._winAdd)
        self.textEdit.setGeometry(QtCore.QRect(10, 270, 331, 41))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(parent=self._winAdd)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.combo = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.combo.setObjectName("combo")
        self.verticalLayout.addWidget(self.combo)
        self.combo.addItem('asfdghj')

        self.listWidget = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(parent=self._winAdd)
        self.pushButton.setGeometry(QtCore.QRect(360, 280, 31, 23))
        self.pushButton.setObjectName("addButton")

        QtCore.QMetaObject.connectSlotsByName(self._winAdd)

        _translate = QtCore.QCoreApplication.translate
        self._winAdd.setWindowTitle(_translate("Form", "Chat"))

        self.pushButton.setText('>')
        self.pushButton.clicked.connect(self.send)

        self.combo.currentTextChanged.connect(self.render_ch)

        self.combo.setFixedHeight(25)



    def show(self, u_id, p_id):
        self.user_id = u_id
        self.proj_id = p_id
        self.query = requests.get(f"{BASE_URL}/list_proj_users/{self.proj_id}").json()
        self.combo.clear()
        if len(self.query) > 0:
            for i in self.query:
                if i['id'] != self.user_id:
                    self.combo.addItem(i['FIO'])
        else:
            self.combo.addItem('nothing to show')

        self.render_ch()
        self._winAdd.show()



    def send(self):
        r_id = 0
        for i in self.query:
            if self.combo.currentText() == i['FIO']:
                r_id = i['id']

        data = {
            'date': str(QtCore.QDate.currentDate().toPyDate()),
            'time': str(QtCore.QTime.currentTime().toPyTime().strftime('%H:%M:%S')),
            'sender_id': self.user_id,
            'reciever_id': r_id,
            'message': str(self.textEdit.toPlainText())
        }
        query = requests.post(f'{BASE_URL}/chat', json=data)
        self.textEdit.clear()
        self.render_ch()


    def get_sender(self, id):
        for i in self.query:
            if i['id'] == id:
                return i['FIO']

    def render_ch(self):
        self.listWidget.clear()
        r_id = 0
        for i in self.query:
            if self.combo.currentText() == i['FIO']:
                r_id = i['id']
        query = requests.get(f'{BASE_URL}/history_chat?sender_id={self.user_id}&reciever_id={r_id}')

        self.sort_hist = sorted(query.json(), key=lambda x: (x['date'], x['time']))

        for i in self.sort_hist:
            time = i['time'].split(':')
            date = datetime.strptime(i['date'], '%Y-%m-%d').date().strftime("%d.%m.%Y")
            self.listWidget.addItem(f'{date} {time[0]}:{time[1]}   {self.get_sender(i['sender_id'])}\n {i['message']}')




