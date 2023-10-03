import sqlite3


class Data():
    @classmethod
    def create__(cls):
        connection = sqlite3.connect('data/tasks.db')
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT
        )''')


    @classmethod
    def add_task(cls,date, time, title, description):
        connection = sqlite3.connect('data/tasks.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Tasks (date, time, title, description) VALUES (?,?,?,?)', (date, time, title, description,))
        connection.commit()
        connection.close()


    @classmethod
    def edit_task(cls,task_id, status):
        connection = sqlite3.connect('data/tasks.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
        connection.commit()
        connection.close()


    @classmethod
    def list_tasks(cls):
        connection = sqlite3.connect('data/tasks.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Tasks')
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
        connection.close()

    @classmethod
    def clear__(cls):
        connection = sqlite3.connect('data/tasks.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Tasks')
        connection.commit()
        connection.close()

