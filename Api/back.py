from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base

__all__ = ['Tasks', 'User', 'session', 'Chat', 'Project', 'Request']

engine = create_engine('sqlite:///db.db')

Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Integer)
    user_id = Column(Integer, ForeignKey('Users.id'))



class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    FIO = Column(String(100), nullable=False)
    login = Column(String(20), nullable=False)
    password = Column(String(16), nullable=False)
    root = Column(Text, nullable=False, default='user')



class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('Users.id'))
    reciever_id = Column(Integer, ForeignKey('Users.id'))
    message = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    desc = Column(String, nullable=False)

class Request(Base):
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('Users.id'))
    reciever_id = Column(Integer, ForeignKey('Users.id'))
    task_id = Column(Integer, ForeignKey('Tasks.id'))


Base.metadata.create_all(engine)

Sessionlocal = sessionmaker(bind=engine)
session = Sessionlocal()
