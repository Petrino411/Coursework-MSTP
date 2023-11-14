import logging
import sys

from fastapi import FastAPI, Request, Body, HTTPException
from back import *
from sqlalchemy import and_
from datetime import datetime, date

app = FastAPI()


@app.get('/list_tasks')
async def list_tasks():
    return session.query(Tasks).all()


@app.get('/auth')
async def auth(login, password):
    try:
        return session.query(User).filter(and_(User.login == login, User.password == password)).one()
    except Exception as e:
        print('Ошибка:', e)


@app.get('/list_tasks_by_date')
async def list_tasks_by_date(date, user_id):
    try:
        return session.query(Tasks).filter(and_(Tasks.date == date, Tasks.user_id == user_id)).all()
    except Exception as e:
        print('Ошибка:', e)

@app.get('/list_tasks_by_id/{task_id}')
async def list_tasks_by_date(task_id):
    try:
        return session.query(Tasks).where(Tasks.id == task_id).one()
    except Exception as e:
        print('Ошибка:', e)


@app.get('/list_users')
async def list_tasks():
    return session.query(User).all()


@app.post('/add')
async def add(data=Body()):
    try:
        task = Tasks(date=datetime.strptime(data["date"], '%Y-%m-%d').date(),
                     time=datetime.strptime(data["time"], '%H:%M:%S').time(),
                     title=data["title"], description=data["description"], status=data["status"],
                     user_id=data["user_id"])
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
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
