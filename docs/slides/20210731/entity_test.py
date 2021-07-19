from abc import ABCMeta, abstractmethod
import unittest

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from enum import Enum

Base = declarative_base()


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        name = Name(first='柿木', last='勝之')
        address = Address(postal_code=PostalCode('722-001'), prefecture='広島県',
                          city='広島市', town='横川町1-2-3', room='123')
        role = Role.管理者
        self.user = User(name, address, role)

    def test_名前を登録できる(self):
        self.assertEqual(str(self.user.name), '柿木 勝之')

    def test_住所を登録できる(self):
        self.assertEqual(str(self.user.address), '722-001 広島県広島市横川町1-2-3 123')

    def test_郵便局を登録できる(self):
        self.assertTrue(self.user.address.postal_code == PostalCode('722-001'))

    def test_権限を登録できる(self):
        self.assertEqual(self.user.role, Role.管理者)


class TestRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = SQLiteRepository()

        name = Name(first='柿木', last='勝之')
        address = Address(postal_code=PostalCode('722-001'), prefecture='広島県',
                          city='広島市', town='横川町1-2-3', room='123')
        self.user = User(name, address)
        self.repo.add(self.user)

    def test_ユーザを登録できる(self):
        self.assertEqual(str(self.repo.get(1).name), '柿木 勝之')
        self.assertEqual(self.repo.get(1).address.postal_code,
                         PostalCode('722-001'))

    def test_該当する条件のユーザを検索できる(self):
        name = Name(first='柿木', last='カツオ')
        address = Address(postal_code=PostalCode('163-8001'), prefecture='東京都',
                          city='新宿区', town='西新宿2-8-1', room='')
        user = User(name, address)
        self.repo.add(user)

        result = self.repo.select_by_address(address)
        self.assertEqual(result.count(), 1)
        self.assertEqual(result.first().name, name)
        self.assertEqual(result.first().address, address)

        result = self.repo.select_by_first_name(name)
        self.assertEqual(result.count(), 2)
        self.assertEqual(result.first().name.last, '勝之')
        self.assertEqual(result[-1].name.last, 'カツオ')

        result = self.repo.select_by_role_admin()
        self.assertEqual(result.count(), 0)


class Role(Enum):
    管理者 = 1
    利用者 = 2


class PostalCode:
    def __init__(self, value):
        self.value = value

    def __eq__(self, o: object) -> bool:
        return self.value == o.value


class Address:
    def __init__(self, postal_code, prefecture, city, town, room):
        self.postal_code = postal_code
        self.prefecture = prefecture
        self.city = city
        self.town = town
        self.room = room

    def __str__(self) -> str:
        return '{} {}{}{} {}'.format(self.postal_code.value, self.prefecture, self.city, self.town, self.room)

    def __eq__(self, o: object) -> bool:
        return self.postal_code == o.postal_code and self.prefecture == o.prefecture and \
               self.city == o.city and self.town == o.town and self.room == o.room

    def __hash__(self) -> int:
        return hash(self.postal_code)

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self) -> str:
        return '{} {}'.format(self.first, self.last)

    def __eq__(self, o: object) -> bool:
        return self.first == o.first and self.last == o.last

    def __hash__(self) -> int:
        return hash(self.first) + hash(self.last)


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
    role_type = Column(Integer)

    def __init__(self, name, address, role=Role.利用者):
        super().__init__()
        self.first_name = name.first
        self.last_name = name.last
        self.postal_code = address.postal_code.value
        self.prefecture = address.prefecture
        self.city = address.city
        self.town = address.town
        self.room = address.room
        self.role_type = role.value

    @property
    def name(self):
        return Name(self.first_name, self.last_name)

    @property
    def address(self):
        return Address(PostalCode(self.postal_code), self.prefecture, self.city, self.town, self.room)

    @property
    def role(self):
        return Role(self.role_type)


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

    def select_by_address(self, address):
        return self.session.query(User).filter(
            User.postal_code == address.postal_code.value,
            User.prefecture == address.prefecture,
            User.city == address.city,
            User.town == address.town,
            User.room == address.room
            )

    def select_by_first_name(self, name):
        return self.session.query(User).filter(
            User.first_name == name.first,
            )

    def select_by_role_admin(self):
        return self.session.query(User).filter(User.role_type == Role.管理者.value)