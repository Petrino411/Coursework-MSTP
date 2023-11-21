from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(411, 320)
        self.textEdit = QtWidgets.QTextEdit(parent=self)
        self.textEdit.setGeometry(QtCore.QRect(10, 270, 331, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(parent=self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setGeometry(QtCore.QRect(360, 280, 31, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")


        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Chat"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ch = Chat()
    ch.show()
    sys.exit(app.exec())
