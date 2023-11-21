from PyQt6 import QtCore, QtWidgets
from project import Project

class Note(Project):
    def __init__(self):
        super().__init__()
        self.pushButton.hide()
        self.pushButton_2.hide()