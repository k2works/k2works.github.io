import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from enum import Enum

Base = declarative_base()


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.name = Name(first='ルー', last='大柴')
        self.address = Adress(zip='123-4567',
                              prefecture='都道府県', city='市町村', house_number='番地')

    def test_名前を登録できる(self):
        user = User(self.name)
        self.assertEqual(str(user.name), 'ルー 大柴')

    def test_住所を登録できる(self):
        user = User(self.name, self.address)
        self.assertEqual(user.address.zip, '123-4567')
        self.assertEqual(str(user.address), '都道府県 市町村 番地')

    def test_役割を登録できる(self):
        user = User(self.name, self.address, Role.ADMIN)
        self.assertEqual(user.role, Role.ADMIN)


class TestRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repository()
        self.name = Name(first='高木', last='ブー')
        self.address = Adress(zip='123-4567',
                              prefecture='都道府県', city='市町村', house_number='番地')
    
    def tearDown(self) -> None:
        self.repo.close()
        self.repo.drop()

    def test_ユーザを登録できる(self):
        user = User(self.name, self.address)
        self.repo.save(user)
        self.repo.commit()
        result = self.repo.find()
        self.assertEqual(str(result.name), '高木 ブー')
        self.assertEqual(result.first_name, '高木')
        self.assertEqual(result.last_name, 'ブー')

    def test_ユーザを検索できる(self):
        user = User(self.name, self.address)
        self.repo.save(user)
        self.repo.commit()
        result = self.repo.find_by_name(self.name)
        self.assertEqual(str(result.name), '高木 ブー')


class Name:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    def __str__(self):
        return '{} {}'.format(self.__first, self.__last)


class Adress:
    def __init__(self, zip, prefecture=None, city=None, house_number=None):
        self.__zip = zip
        self.__prefecture = prefecture
        self.__city = city
        self.__house_number = house_number

    @property
    def zip(self):
        return self.__zip

    @property
    def prefecture(self):
        return self.__prefecture

    @property
    def city(self):
        return self.__city

    @property
    def house_number(self):
        return self.__house_number

    def __str__(self):
        return '{} {} {}'.format(self.__prefecture, self.__city, self.__house_number)


class Role(Enum):
    ADMIN = 1
    USER = 2


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    zip = Column(String)
    prefecture = Column(String)
    city = Column(String)
    house_number = Column(String)
    role_code = Column(Integer)


    def __init__(self, name, address=None, role=Role.USER) -> None:
        super().__init__()
        self.first_name = name.first
        self.last_name = name.last
        if not address == None:
            self.zip = address.zip
            self.prefecture = address.prefecture
            self.city = address.city
            self.house_number = address.house_number
        self.role_code = role.value

    @property
    def name(self):
        return Name(first=self.first_name, last=self.last_name)

    @property
    def address(self):
        return Adress(zip=self.zip, prefecture=self.prefecture, city=self.city, house_number=self.house_number)

    @property
    def role(self):
        return Role(self.role_code)


class Repository:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///db.sqlite')
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        Base.metadata.create_all(self.engine)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()

    def drop(self):
        User.__table__.drop(self.engine)

    def save(self, user):
        self.session.add(user)

    def find(self):
        return self.session.query(User).first()

    def find_by_name(self, name):
        return self.session.query(User).filter_by(first_name=name.first, last_name=name.last).first()


unittest.main(argv=[''], verbosity=2, exit=False)
