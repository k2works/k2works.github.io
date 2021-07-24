from abc import ABCMeta, abstractmethod
import unittest
from unittest.case import doModuleCleanups
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from enum import Enum

from sqlalchemy.sql.functions import percent_rank

Base = declarative_base()

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        name = Name(first="柿木",last="勝之")
        postal_code = PostalCode("733-0011")
        address = Address(postal_code, prefecture="広島県",
                          city="広島市西区", twon="横川町1-2-3", room="123")
        self.user = User(name, address, role=Role.管理者)

    def test_名前を登録できる(self):
        self.assertEqual(str(self.user.name), "柿木 勝之")

    def test_住所を登録できる(self):
        self.assertEqual(str(self.user.address),
                         "733-0011 広島県広島市西区横川町1-2-3 123")
        self.assertEqual(str(self.user.address.postal_code), "733-0011")

    def test_権限を登録できる(self):
        self.assertEqual(self.user.role, Role.管理者)


class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        name = Name(first="柿木", last="勝之")
        postal_code = PostalCode("733-0011")
        address = Address(postal_code, prefecture="広島県",
                          city="広島市西区", twon="横川町1-2-3", room="123")
        user = User(name, address)
        repo = SQLiteRepository()
        repo.add_user(user)

        self.assertEqual(repo.get_user(1).name, name)
        self.assertEqual(repo.get_user(1).address, address)
        self.assertEqual(repo.get_user(1).address.postal_code, postal_code)
        self.assertEqual(repo.get_user(1).postal_code, postal_code.value)
        self.assertEqual(repo.get_user(1).role, Role.利用者)
        self.assertEqual(repo.get_user(1).role_type, Role.利用者.value)


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


class PostalCode:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

    def __eq__(self, o: object) -> bool:
        return self.value == o.value

    def __hash__(self) -> int:
        return hash(self.value)


class Address:
    def __init__(self, postal_code: PostalCode, prefecture: str, city: str, twon: str, room: str) -> None:
        self.postal_code = postal_code
        self.prefecture = prefecture
        self.city = city
        self.twon = twon
        self.room = room

    def __str__(self) -> str:
        return f"{self.postal_code} {self.prefecture}{self.city}{self.twon} {self.room}"

    def __eq__(self, o: object) -> bool:
        return self.postal_code == o.postal_code and self.prefecture == o.prefecture and self.city == o.city and self.twon == o.twon and self.room == o.room

    def __hash__(self) -> int:
        return hash(self.postal_code) ^ hash(self.prefecture) ^ hash(self.city) ^ hash(self.twon) ^ hash(self.room)


class Role(Enum):
    管理者 = 1
    利用者 = 2

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    prefecture = Column(String)
    city = Column(String)
    twon = Column(String)
    room = Column(String)
    role_type = Column(Integer)

    def __init__(self, name: Name, address: Address, role=Role.利用者):
        self.last_name = name.last
        self.first_name = name.first
        self.postal_code = address.postal_code.value
        self.prefecture = address.prefecture
        self.city = address.city
        self.twon = address.twon
        self.room = address.room
        self.role_type = role.value

    @property
    def name(self):
        return Name(first=self.first_name, last=self.last_name)

    @property
    def address(self):
        return Address(postal_code=PostalCode(self.postal_code), prefecture=self.prefecture, city=self.city, twon=self.twon, room=self.room)

    @property
    def role(self):
        return Role(self.role_type)


class Repository(metaclass=ABCMeta):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def get_user(self, index):
        pass

class SQLiteRepository(Repository):
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
