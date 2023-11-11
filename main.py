from pathlib import Path

from PyQt6.QtCore import QDateTime, QTime

from todo import *
from add import *
from back import *
from auth import Login

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet(Path('style.сss').read_text())
    auth_window = Login()
    auth_window.show()


    cur = QDateTime.currentDateTime().time()
    for i in db.list_tasks():
        s = i[2].split(':')
        time = QTime(int(s[0]), int(s[1]), int(s[2]))
        if cur < time:
            print(i)

    sys.exit(app.exec())
