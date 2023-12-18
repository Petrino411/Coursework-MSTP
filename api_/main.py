from fastapi import FastAPI, Body, HTTPException
from sqlalchemy.exc import NoResultFound

from back import *
from sqlalchemy import and_, or_
from datetime import datetime

app = FastAPI()


class DataRequests:
    @staticmethod
    @app.get('/connection')
    async def connection():
        return True

    @staticmethod
    @app.get('/list_projects')
    async def list_projects():
        return session.query(Project).all()

    @staticmethod
    @app.get('/auth')
    async def auth(login, password):
        try:
            return session.query(User).filter(and_(User.login == str(login), User.password == str(password))).one()
        except NoResultFound as e:
            raise HTTPException(status_code=404, detail=str(e))

    @staticmethod
    @app.get('/list_tasks_by_date')
    async def list_tasks_by_date(date, proj_id):
        try:
            return session.query(Tasks).filter(
                and_(Tasks.date == date, Tasks.project_id == proj_id)).all()
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.get('/get_name_for_notes')
    async def get_name_for_notes(task_id):
        try:
            q = session.query(Request).filter(Request.task_id == task_id).first()
            u = session.query(User).filter(User.id == q.sender_id).one()
            return u.FIO
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.get('/list_tasks_by_id/{task_id}')
    async def list_tasks_by_id(task_id):
        try:
            return session.query(Tasks).where(Tasks.id == task_id).one()
        except Exception as e:
            return e

    @staticmethod
    @app.get('/profile/{user_id}')
    async def profile(user_id):
        try:
            return session.query(User).where(User.id == user_id).one()
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.get('/project/{user_id}')
    async def project(user_id):
        try:
            return session.query(Project).where(
                and_(User_project.project_id == Project.id, User_project.user_id == user_id)).all()
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.get('/project_for_admin')
    async def project_for_admin():
        try:
            return session.query(Project).all()
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.get('/list_users')
    async def list_users(user_id):
        return session.query(User).filter(User.id == user_id).one()

    @staticmethod
    @app.get('/history_chat')
    async def history_chat(sender_id, reciever_id):
        return session.query(Chat).where(and_(or_(Chat.reciever_id == sender_id, Chat.reciever_id == reciever_id),
                                              or_(Chat.sender_id == sender_id, Chat.sender_id == reciever_id))).all()

    @staticmethod
    @app.get('/list_notes')
    async def list_notes(u_id):
        query = session.query(Tasks).where(Tasks.user_id == u_id).all()
        return query

    @staticmethod
    @app.get('/list_proj_users/{project_id}')
    async def list_proj_users(project_id):
        return session.query(User).where(
            and_(User_project.user_id == User.id, User_project.project_id == project_id)).all()

    @staticmethod
    @app.post('/add')
    async def add(data=Body()):
        try:
            task = Tasks(date=datetime.strptime(data["date"], '%Y-%m-%d').date(),
                         time=datetime.strptime(data["time"], '%H:%M:%S').time(),
                         title=data["title"], description=data["description"], status=data["status"],
                         user_id=data["user_id"],
                         project_id=data['project_id'])
            session.add(task)
            session.commit()
            session.refresh(task)
            return task
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.post('/add_project/{user_ud}')
    async def add_project(user_ud, data=Body()):
        try:
            pr = Project(
                name=data["name"], desc=data["desc"])
            session.add(pr)
            session.commit()
            session.refresh(pr)

            pr_user = User_project(user_id = user_ud, project_id = pr.id)
            session.add(pr_user)
            session.commit()
            session.refresh(pr_user)
            return pr

        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.post('/user_to_project')
    async def user_to_project(data=Body()):
        try:
            u_p = User_project(user_id=data["user_id"], project_id=data["project_id"])
            session.add(u_p)
            session.commit()
            session.refresh(u_p)
            return u_p
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.post('/add2')
    async def add2(data=Body()):
        try:
            req = Request(sender_id=data["sender_id"], task_id=data['task_id'])
            session.add(req)
            session.commit()
            session.refresh(req)
            return req
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.post('/add_user')
    async def add_user(data=Body()):
        try:
            user = User(FIO=data["FIO"], login=data["login"], password=data["password"], root=data["root"])
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.post('/chat')
    async def chat(data=Body()):
        try:
            ch = Chat(sender_id=data['sender_id'],
                      reciever_id=data['reciever_id'],
                      message=data["message"], date=datetime.strptime(data["date"], '%Y-%m-%d').date(),
                      time=datetime.strptime(data["time"], '%H:%M:%S').time())
            session.add(ch)
            session.commit()
            session.refresh(ch)
            return ch
        except Exception as e:
            print('Ошибка:', e)

    @staticmethod
    @app.put('/edit/{task_id}')
    async def edit(task_id: int, data=Body()):
        # Получаем задачу по идентификатору
        task = session.query(Tasks).filter_by(id=task_id).one()

        # Проверяем, найдена ли задача
        if task is None:
            raise HTTPException(status_code=404, detail="Задача не найдена")
        # Обновляем поля задачи
        if "date" in data:
            task.date = datetime.strptime(data["date"], '%Y-%m-%d').date()
        if "time" in data:
            task.time = datetime.strptime(data["time"], '%H:%M:%S').time()
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "status" in data:
            task.status = data["status"]
        if "user_id" in data:
            task.user_id = data["user_id"]

        # Фиксируем изменения в базе данных
        session.commit()
        session.refresh(task)

        return task

    @staticmethod
    @app.put('/update_st')
    async def update_st(task_id: int, st):
        task = session.query(Tasks).filter_by(id=task_id).one()

        # Проверяем, найдена ли задача
        if task is None:
            raise HTTPException(status_code=404, detail="Задача не найдена")
        # Обновляем поля задачи
        task.status = st

        session.commit()
        session.refresh(task)

        return task

    @staticmethod
    @app.put('/update_profile')
    async def update_profile(data=Body()):
        pr = session.query(User).filter_by(id=data['id']).one()

        # Проверяем, найдена ли задача
        if pr is None:
            raise HTTPException(status_code=404, detail="Задача не найдена")
        # Обновляем поля задачи
        if "FIO" in data:
            pr.FIO = data['FIO']
        if "login" in data:
            pr.login = data['login']
        if "password" in data:
            pr.password = data['password']

        session.commit()
        session.refresh(pr)

        return pr

    @staticmethod
    @app.delete("/tasks/{task_id}")
    async def delete_item(task_id: int):
        item = session.query(Tasks).filter(Tasks.id == task_id).one()
        req = session.query(Request).filter(Request.task_id == task_id).all()

        session.delete(item)
        for i in req:
            session.delete(i)
        session.commit()

    @staticmethod
    @app.delete("/project/{name}")
    async def delete_project_id(name: str):
        item = session.query(Project).filter(Project.name == str(name)).one()
        u_p = session.query(User_project).filter(User_project.project_id == item.id).all()
        t_p = session.query(Tasks).filter(Tasks.project_id == item.id).all()
        session.delete(item)
        for i in t_p:
            session.delete(i)
        for i in u_p:
            u = session.query(User).filter(User.id == i.user_id).one()
            ch = session.query(Chat).where(or_(Chat.reciever_id == u.id, Chat.reciever_id == u.id)).all()
            for i in ch:
                session.delete(i)
            session.delete(i)
            if u.root != 'admin':
                session.delete(u)


        session.commit()
