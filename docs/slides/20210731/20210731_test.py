import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class TestUser(unittest.TestCase):
    def test_名前を登録できる(self):
        user = User(name='ユーザ名')
        self.assertEqual(user.name, 'ユーザ名')

    def test_住所を登録できる(self):
        user = User(name='ユーザー名', zip='123-4567', address='住所')
        self.assertEqual(user.zip, '123-4567')
        self.assertEqual(user.address, '住所')


class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        user = User(name='ユーザ名', zip='123-4567', address='住所')
        repo = Repository()
        repo.save(user)
        result = repo.find()
        self.assertEqual(result.name, 'ユーザ名')

    def test_ユーザを検索できる(self):
        user = User(name='ユーザ名', zip='123-4567', address='住所')
        repo = Repository()
        repo.save(user)
        result = repo.find_by_name('ユーザ名')
        self.assertEqual(result.name, 'ユーザ名')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    zip = Column(String)
    address = Column(String)


class Repository:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///:memory:')
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.engine.connect()
        Base.metadata.create_all(self.engine)

    def save(self, user):
        self.session.add(user)

    def find(self):
        return self.session.query(User).first()

    def find_by_name(self, name):
        return self.session.query(User).filter_by(name=name).first()


unittest.main(argv=[''], verbosity=2, exit=False)
