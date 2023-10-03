import sqlite3


class Data():
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('data/tasks.db')
        self.cursor = self.connection.cursor()

        # Создаем таблицу Tasks
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT
        )''')


        # Функция для добавления новой задачи

    def add_task(self,date, time, title, description):
        self.cursor.execute('INSERT INTO Tasks (date, time, title, description) VALUES (?,?,?,?)', (date, time, title, description,))
        self.connection.commit()


    # Функция для обновления статуса задачи

    def edit_task(self,task_id, status):
        self.cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
        self.connection.commit()


    # Функция для вывода списка задач

    def list_tasks(self,):
        self.cursor.execute('SELECT * FROM Tasks')
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(task)



        self.connection.close()