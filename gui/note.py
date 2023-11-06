from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget




class Note(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(385, 90)
        self.setStyleSheet("background-color: rgb(23, 33, 43);")
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(10, 0, 371, 81))
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setGeometry(QtCore.QRect(360, 0, 21, 21))
        self.pushButton.setStyleSheet("QPushButton{\n"
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

        self.pushButton.setText("")
        self.pushButton.clicked.connect(self.close)

        available_geometry = QtGui.QGuiApplication.primaryScreen().availableGeometry()

        # Устанавливаем окно справа снизу над панелью задач
        self.move(available_geometry.right() - self.width(), available_geometry.bottom() - self.height())

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/ico/close_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    n = Note()
    n.show()
    sys.exit(app.exec())
