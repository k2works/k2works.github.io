import unittest


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
        repo = Repository()
        repo.add(user)
        self.assertEqual(repo.get(user.name), user)

class User:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

class Repository:
    def __init__(self):
        self.__users = {}

    def add(self, user):
        self.__users[user.name] = user

    def get(self, name):
        return self.__users[name]
