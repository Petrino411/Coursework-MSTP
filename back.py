import sqlite3


class Data:
    connection = sqlite3.connect('data/tasks.db')
    cursor = connection.cursor()
    object = None

    def __new__(cls, *args, **kwargs):
        if cls.object == None:
            cls.object = object.__new__(cls)
        return cls.object

    """Создание таблицы"""
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

    """Добавление дела"""
    @classmethod
    def add_task(cls, date, time, title, description):
        cls.cursor.execute('INSERT INTO Tasks (date, time, title, description) VALUES (?,?,?,?)',
                           (date, time, title, description,))
        cls.connection.commit()

    @classmethod
    def edit_task(cls):
        None

    """Вывод всех дел"""
    @classmethod
    def list_tasks(cls):
        cls.cursor.execute('SELECT * FROM Tasks')
        tasks = cls.cursor.fetchall()
        for task in tasks:
            print(task)

    """Очистка таблицы"""
    @classmethod
    def clear__(cls):
        cls.cursor.execute('DELETE FROM Tasks')
        cls.connection.commit()

    """Выборка из таблицы по дате"""
    @classmethod
    def get_List_tasks(cls, date) -> list[tuple]:
        query = 'SELECT time, title, description FROM Tasks WHERE Date = ?'
        cls.cursor.execute(query, (date,))
        tasks = cls.cursor.fetchall()
        return tasks

    @classmethod
    def remove(cls, title):
        query = 'DELETE FROM Tasks WHERE title = ?'
        cls.cursor.execute(query, (title,))
        cls.connection.commit()

    @classmethod
    def edit(cls, value: list[str]):
        value = tuple(value)
        query = 'UPDATE Tasks SET date = ?, time = ?, title = ?, description = ? WHERE title = ?'
        cls.cursor.execute(query, (value[0], value[1], value[2], value[3], value[4],))
        cls.connection.commit()

    def __del__(self):
        self.connection.close()


db = Data()