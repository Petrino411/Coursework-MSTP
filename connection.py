BASE_URL = 'https://eb14-188-32-236-22.ngrok-free.app'

def chat_open(self):
    idd = self.user["id"]
    self.name_user = self.comboBox.currentText()
    if self.name_user == "":
        self.id_user = self.user["id"]
        else:
        self.id_user = self.people_cl[self.name_user]    #answer = requests.get(f"http://127.0.0.1:8000/chatt")
        answer = requests.get(f"{url}/chat?id_sender={idd}&id_recipient={self.id_user}")    messg = answer.json()
    mee = []
    for i in range(len(messg)):        i
        if messg[i]["id_sender"] == self.user["id"]:
            name = "Вы"
        else:
            name = self.name_user
        mee.append("\t\t\t\t" + messg[i]["time"] + "\n" + name + ": " + messg[i]["message"] + "\n")
        # mee.append("\t\t\t\t" + messg2[i]["time"] + "\n" + name + ": " + messg2[i]["message"] + "\n")    self.plainTextEdit.setText("\n".join(mee))
        cursor = self.plainTextEdit.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.plainTextEdit.setTextCursor(cursor)
        self.plainTextEdit.ensureCursorVisible()
    return "\n".join(mee)