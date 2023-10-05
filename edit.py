from PyQt6.QtWidgets import QDialog

from add import *


class Edit(Add):
    def __init__(self):
        super().__init__()

        self.titleFIRST = None
        _translate = QtCore.QCoreApplication.translate
        self._winAdd.setWindowTitle(_translate("Form", "Edit"))
        self.pushButton.setText(_translate("Form", "Edit"))

    def execute(self):
        if self.titleLineEdit.text() != '':
            data = []
            data.append(str(self.dateEdit.date().toPyDate()))
            data.append(str(self.timeEdit.time().toPyTime()))
            data.append(str(self.titleLineEdit.text()))
            data.append(str(self.descEdit.toPlainText()))
            data.append(str(self.titleFIRST))
            db.edit(data)
            self._winAdd.hide()
            self.titleLineEdit.clear()
            self.descEdit.clear()

    def show(self, line: list[QtCore.QDate, tuple[str]]) -> None:
        self.dateEdit.setDate(line[0])
        self.timeEdit.setTime(QtCore.QTime.fromString(line[1][0]))
        self.titleLineEdit.setText(line[1][1])

        self.titleFIRST = line[1][1]
        self.descEdit.setText(line[1][2])
        self._winAdd.show()
