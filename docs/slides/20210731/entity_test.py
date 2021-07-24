import unittest
from unittest.case import doModuleCleanups
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from enum import Enum

Base = declarative_base()

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        name = Name(first="柿木",last="勝之")
        self.user = User(name, role=Role.管理者)
        self.user.address = "733-0011 広島県広島市西区横川町1-2-3 123"

    def test_名前を登録できる(self):
        self.assertEqual(str(self.user.name), "柿木 勝之")

    def test_住所を登録できる(self):
        self.assertEqual(self.user.address, "733-0011 広島県広島市西区横川町1-2-3 123")

    def test_権限を登録できる(self):
        self.assertEqual(self.user.role, Role.管理者)

class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        name = Name(first="柿木",last="勝之")
        user = User(name)
        user.address = "733-0011 広島県広島市西区横川町1-2-3 123"
        repo = SQLiteRepository()
        repo.add_user(user)

        self.assertEqual(repo.get_user(1).name, name)
        self.assertEqual(repo.get_user(1).address, "733-0011 広島県広島市西区横川町1-2-3 123")
        self.assertEqual(repo.get_user(1).role, Role.利用者)


class Name:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    def __str__(self) -> str:
        return f"{self.first} {self.last}"

    def __eq__(self, o: object) -> bool:
        return self.first == o.first and self.last == o.last

    def __hash__(self) -> int:
        return hash(self.first) ^ hash(self.last)

class Role(Enum):
    管理者 = 1
    利用者 = 2

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    role_type = Column(Integer)

    def __init__(self, name: Name, role=Role.利用者):
        self.last_name = name.last
        self.role_type = role.value
        self.first_name = name.first

    @property
    def name(self):
        return Name(first=self.first_name, last=self.last_name)

    @property
    def role(self):
        return Role(self.role_type)


class Repository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, index):
        return self.users[index]

class SQLiteRepository:
    def __init__(self):
        self.engine = create_engine("sqlite:///:memory:")
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        Base.metadata.create_all(self.engine)

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    def get_user(self, index):
        return self.session.query(User).get(index)