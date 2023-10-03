from add import *

class Edit(Add):
    def __init__(self):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Edit"))
        self.pushButton.setText(_translate("Form", "Edit"))