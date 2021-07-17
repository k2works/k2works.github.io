import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from abc import ABCMeta, abstractmethod

Base = declarative_base()


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User(name="高木 ブー", address="733-0000 広島県広島市西区横川町1-2-3")

    def test_名前を登録できる(self):
        self.assertEqual(self.user.name, "高木 ブー")

    def test_住所を登録できる(self):
        self.assertEqual(self.user.address, "733-0000 広島県広島市西区横川町1-2-3")


class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        user = User(name="高木 ブー", address="733-0000 広島県広島市西区横川町1-2-3")
        repo = SQLiteRepositry()
        repo.add(user)
        self.assertEqual(repo.get(user.name), user)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)


class Repository(metaclass = ABCMeta):
    @abstractmethod
    def add(self, user):
        pass
    @abstractmethod
    def get(self, name):
        pass 


class SQLiteRepositry(Repository):
    def __init__(self):        
        super().__init__()
        self.engine = create_engine('sqlite:///:memory:')
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        Base.metadata.create_all(self.engine)

    def add(self, user):
        self.session.add(user)

    def get(self, name):
        return self.session.query(User).filter_by(name=name).first()
