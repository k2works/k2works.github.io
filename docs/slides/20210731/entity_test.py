import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from abc import ABCMeta, abstractmethod
from enum import Enum

Base = declarative_base()


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User(name=Name(first="高木", last="ブー"),
                         address=Address(postal_code="733-0000", prefecture="広島県", city="広島市西区", town="横川町1-2-3"), role=Role.管理者)

    def test_名前を登録できる(self):
        self.assertEqual(str(self.user.name), "高木 ブー")

    def test_住所を登録できる(self):
        self.assertEqual(str(self.user.address), "733-0000 広島県広島市西区横川町1-2-3")

    def test_役割を登録できる(self):
        self.assertEqual(self.user.role, Role.管理者)


class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        user = User(name=Name(first="高木", last="ブー"),
                    address=Address(postal_code="733-0000", prefecture="広島県", city="広島市西区", town="横川町1-2-3"))
        repo = SQLiteRepositry()
        repo.add(user)
        self.assertEqual(repo.get(user.name), user)


class Name:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    def __str__(self) -> str:
        return "{} {}".format(self.__first, self.__last)

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

class Role(Enum):
    管理者 = 1
    利用者 = 2


class Address:
    def __init__(self, postal_code, prefecture, city, town):
        self.__postal_code = postal_code
        self.__prefecture = prefecture
        self.__city = city
        self.__town = town

    @property
    def postal_code(self):
        return self.__postal_code

    @property
    def prefecture(self):
        return self.__prefecture

    @property
    def city(self):
        return self.__city

    @property
    def town(self):
        return self.__town

    def __str__(self) -> str:
        return "{} {}{}{}".format(self.__postal_code, self.__prefecture, self.__city, self.__town)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    postal_code = Column(String)
    prefecture = Column(String)
    city = Column(String)
    town = Column(String)
    role_no = Column(Integer)

    def __init__(self, name: Name, address: str, role: str = Role.利用者):
        super().__init__()
        self.first_name = name.first
        self.last_name = name.last
        self.postal_code = address.postal_code
        self.prefecture = address.prefecture
        self.city = address.city
        self.town = address.town
        self.role_no = role.value

    @property
    def name(self) -> Name:
        return Name(self.first_name, self.last_name)

    @property
    def address(self) -> Address:
        return Address(self.postal_code, self.prefecture, self.city, self.town)

    @property
    def role(self) -> Role:
        return Role(self.role_no)


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
        return self.session.query(User).filter_by(first_name=name.first, last_name=name.last).first()
