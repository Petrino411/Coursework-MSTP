from PyQt6 import QtCore, QtWidgets
from project import Project

class Note(Project):
    def __init__(self):
        Project.__init__(self)

        _translate = QtCore.QCoreApplication.translate
        self._proj_win.setWindowTitle(_translate("Form", "Notifications"))
        self.pushButton.setText(_translate("Form", "Accept"))
        self.pushButton_2.setText(_translate("Form", "Deny"))