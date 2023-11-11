from fastapi import FastAPI, Request
from back import *

app = FastAPI()

@app.get('/list_tasks')
async def list_tasks():
    return session.query(Tasks).all()

@app.get('/list_users')
async def list_tasks():
    return session.query(User).all()

@app.post('/test')
async def test(data):
    return data


session.close()


