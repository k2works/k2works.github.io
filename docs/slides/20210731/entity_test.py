import unittest

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class TestUser(unittest.TestCase):
    def test_user(self):
        user = User()
        user.name = '柿木 勝之'
        user.address = '722-001 広島県広島市横川町1-2-3 123'
        self.assertEqual(user.name, '柿木 勝之')


class TestRepository(unittest.TestCase):
    def test_repository(self):
        user = User()
        user.name = '柿木 勝之'
        user.address = '722-001 広島県広島市横川町1-2-3 123'
        repo = SQLiteRepository()
        repo.add(user)
        self.assertEqual(repo.get(1).name, '柿木 勝之')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self):
        super().__init__()


class Repository:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def get(self, index):
        return self.users[index]


class SQLiteRepository:
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        Base.metadata.create_all(self.engine)

    def add(self, user):
        self.session.add(user)

    def get(self, index):
        return self.session.query(User).filter(User.id == index).first()
