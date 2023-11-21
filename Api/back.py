from sqlalchemy import *
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, declarative_base

__all__ = ['Tasks', 'User', 'session']

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

    #def __init__(self, d: dict = None):
    #    if not d:
    #        for i in d.items():
    #            self.__setattr__(i, d[i])

    def __str__(self):
        return f"{self.id}, {self.date}, {self.time}, {self.title}, {self.description}"


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    FIO = Column(String(100), nullable=False)
    login = Column(String(20), nullable=False)
    password = Column(String(16), nullable=False)
    root = Column(Text, nullable=False, default='user')

    #def __init__(self, d: dict = None):
    #    if not d:
    #        for i in d.items():
    #            self.__setattr__(i, d[i])

    def __str__(self):
        return f"{self.id}, {self.date}, {self.time}, {self.title}, {self.description}"


class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, nullable=False)
    reciever_id = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)


Base.metadata.create_all(engine)

Sessionlocal = sessionmaker(bind=engine)
session = Sessionlocal()
