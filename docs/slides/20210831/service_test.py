import unittest
from enum import Enum


class TestUser(unittest.TestCase):
    def test_名前を登録できる(self):
        user = User(name='test', address='')
        self.assertEqual(user.name, 'test')

    def test_住所を登録できる(self):
        user = User(name='test', address='test')
        self.assertEqual(user.address, 'test')

    def test_権限を登録できる(self):
        user = User(name='test', address='test', role=Role.管理者)
        self.assertEqual(user.role, Role.管理者)

class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        repo = Repository()
        user = User(name='test', address='test', role=Role.管理者)
        repo.add(user)
        self.assertEqual(repo.get(user.name), user)

class TestService(unittest.TestCase):
    def test_ユーザを登録できる(self):
        service = Service()
        user = User(name='test', address='test', role=Role.管理者)
        service.save(user)
        self.assertEqual(service.find_by_name(user.name), user)


class Role(Enum):
    管理者 = 1
    利用者 = 2

class User:
    def __init__(self, name, address, role=Role.利用者):
        self.name = name
        self.address = address
        self.role = role

class Repository:
    def __init__(self):
        self.__data = {}

    def add(self, user):
        self.__data[user.name] = user
        return user
    
    def get(self, name):
        return self.__data[name]

class Service:
    def __init__(self):
        self.repository = Repository()

    def save(self, user):
        self.repository.add(user)

    def find_by_name(self, name):
        return self.repository.get(name)

