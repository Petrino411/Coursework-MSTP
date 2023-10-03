import sqlite3


class Data():
    connection = sqlite3.connect('data/tasks.db')
    cursor = connection.cursor()
    object = None

    def __new__(cls, *args, **kwargs):
        if cls.object == None:
            cls.object = object.__new__(cls)
        return cls.object


    @classmethod
    def create__(cls):
        cls.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT
        )''')

    @classmethod
    def add_task(cls, date, time, title, description):
        cls.cursor.execute('INSERT INTO Tasks (date, time, title, description) VALUES (?,?,?,?)',
                           (date, time, title, description,))
        cls.connection.commit()

    @classmethod
    def edit_task(cls, task_id, status):
        cls.cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
        cls.connection.commit()

    @classmethod
    def list_tasks(cls):
        cls.cursor.execute('SELECT * FROM Tasks')
        tasks = cls.cursor.fetchall()
        for task in tasks:
            print(task)

    @classmethod
    def clear__(cls):
        cls.cursor.execute('DELETE FROM Tasks')
        cls.connection.commit()

    @classmethod
    def get_List_tasks(cls, date) -> list[tuple]:
        query = 'SELECT time, title, description FROM Tasks WHERE Date = ?'
        cls.cursor.execute(query, (date,))
        tasks = cls.cursor.fetchall()
        return tasks

    @classmethod
    def remove_task(cls):
        cls.cursor.execute('DELETE FROM Tasks')
        cls.connection.commit()

    def __del__(self):
        self.connection.close()


db = Data()