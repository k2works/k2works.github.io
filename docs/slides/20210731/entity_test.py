from abc import ABCMeta, abstractmethod
import unittest

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class TestUser(unittest.TestCase):
    def test_user(self):
        name = Name(first='柿木', last='勝之')
        address = Address(postal_code='722-001', prefecture='広島県',
                          city='広島市', town='横川町1-2-3', room='123')
        user = User(name, address)
        self.assertEqual(user.name, '柿木 勝之')
        self.assertEqual(user.address, '722-001 広島県広島市横川町1-2-3 123')


class TestRepository(unittest.TestCase):
    def test_repository(self):
        name = Name(first='柿木', last='勝之')
        address = Address(postal_code='722-001', prefecture='広島県',
                          city='広島市', town='横川町1-2-3', room='123')
        user = User(name,address)
        repo = SQLiteRepository()
        repo.add(user)
        self.assertEqual(repo.get(1).name, '柿木 勝之')

class Address:
    def __init__(self, postal_code, prefecture, city, town, room):
        self.postal_code = postal_code
        self.prefecture = prefecture
        self.city = city
        self.town = town
        self.room = room

    def __str__(self) -> str:
        return '{} {}{}{} {}'.format(self.postal_code, self.prefecture, self.city, self.town, self.room)

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self) -> str:
        return '{} {}'.format(self.first, self.last)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    postal_code = Column(String)
    prefecture = Column(String)
    city = Column(String)
    town = Column(String)
    room = Column(String)

    def __init__(self, name, address):
        super().__init__()
        self.first_name = name.first
        self.last_name = name.last
        self.postal_code = address.postal_code
        self.prefecture = address.prefecture
        self.city = address.city
        self.town = address.town
        self.room = address.room

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def address(self):
        return '{} {}{}{} {}'.format(self.postal_code, self.prefecture, self.city, self.town, self.room)


class Repository(metaclass=ABCMeta):
    @abstractmethod
    def add(self, user):
        pass

    @abstractmethod
    def get(self, index):
        pass


class SQLiteRepository(Repository):
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        Base.metadata.create_all(self.engine)

    def add(self, user):
        self.session.add(user)

    def get(self, index):
        return self.session.query(User).filter(User.id == index).first()
