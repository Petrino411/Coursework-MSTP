from fastapi import FastAPI, Request
from back import *
from sqlalchemy import and_

app = FastAPI()

@app.get('/list_tasks')
async def list_tasks():
    return session.query(Tasks).all()

@app.get('/auth')
async def auth(login, password):
    try:
        return session.query(User).filter(and_(User.login == login, User.password == password)).one()
    except:
        print('ошибка')

@app.get('/list_users')
async def list_tasks():
    return session.query(User).all()

@app.post('/test')
async def test(data):
    return data


session.close()


