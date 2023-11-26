from fastapi import FastAPI, Body, HTTPException
from back import *
from sqlalchemy import and_, or_
from datetime import datetime

app = FastAPI()


@app.get('/list_tasks')
async def list_tasks():
    return session.query(Tasks).all()

@app.get('/list_projects')
async def list_projects():
    return session.query(Project).all()


@app.get('/auth')
async def auth(login, password):
    try:
        return session.query(User).filter(and_(User.login == str(login), User.password == str(password))).one()
    except Exception as e:
        print('Ошибка:', e)


@app.get('/list_tasks_by_date')
async def list_tasks_by_date(date, user_id, proj_id):
    try:
        return session.query(Tasks).filter(
            and_(Tasks.date == date, Tasks.user_id == user_id, Tasks.project_id == proj_id)).all()
    except Exception as e:
        print('Ошибка:', e)

@app.get('/get_name_for_notes')
async def get_name_for_notes():
    try:
        return session.query(Request).all()
    except Exception as e:
        print('Ошибка:', e)



@app.get('/list_tasks_by_id/{task_id}')
async def list_tasks_by_date(task_id):
    try:
        return session.query(Tasks).where(Tasks.id == task_id).one()
    except Exception as e:
        print('Ошибка:', e)


@app.get('/profile/{user_id}')
async def profile(user_id):
    try:
        return session.query(User).where(User.id == user_id).one()
    except Exception as e:
        print('Ошибка:', e)


@app.get('/project/{user_id}')
async def project(user_id):
    try:
        return session.query(Project).where(
            and_(User_project.project_id == Project.id, User_project.user_id == user_id)).all()
    except Exception as e:
        print('Ошибка:', e)


@app.get('/list_users')
async def list_users():
    return session.query(User).all()


@app.get('/history_chat')
async def history_chat(sender_id, reciever_id):
    return session.query(Chat).where(and_(or_(Chat.reciever_id == sender_id, Chat.reciever_id == reciever_id), or_(Chat.sender_id == sender_id, Chat.sender_id == reciever_id))).all()


@app.get('/list_notes')
async def list_notes(u_id):
    query = session.query(Tasks).where(Tasks.user_id == u_id).all()
    return query


@app.get('/list_proj_users/{project_id}')
async def list_proj_users(project_id):
    return session.query(User).where(and_(User_project.user_id == User.id, User_project.project_id == project_id)).all()


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

    # Фиксируем изменения в базе данных
    session.commit()
    session.refresh(task)

    return task

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



@app.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
    item = session.query(Tasks).filter(Tasks.id == task_id).one()

    if item:
        session.delete(item)
        session.commit()
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


session.close()

"""
from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
from back import Sessionlocal, Tasks, User

# создаем таблицы


app = FastAPI()


# определяем зависимость
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("public/index.html")


@app.get('/api/list_users')
async def list_tasks(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get('/auth')
async def auth(login, password, db: Session = Depends(get_db)):
    try:
        return db.query(User).filter(and_(User.login == login, User.password == password)).one()
    except:
        print('ошибка')



@app.get('/api/list_tasks_by_date')
async def list_tasks_by_date(date, user_id, db: Session = Depends(get_db)):
    try:
        return db.query(Tasks).filter(and_(Tasks.date == date, Tasks.user_id == user_id)).all()
    except:
        print('ошибка')

@app.post('/add')
async def add(data = Body(), db: Session = Depends(get_db)):
    try:
        task = Tasks(date=data[0], time=data[1], title=data[2], description=data[3], status=data[4], user_id=data[5])
        db.add(task)
        db.commit()
    except:
        print('ошибка')



@app.post("/api/users")
def create_person(data=Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@app.put("/api/users")
def edit_person(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    db.commit()  # сохраняем изменения
    db.refresh(person)
    return person


@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    # если пользователь найден, удаляем его
    db.delete(person)  # удаляем объект
    db.commit()  # сохраняем изменения
    return person"""
