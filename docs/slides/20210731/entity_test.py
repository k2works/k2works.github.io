import unittest

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.user.name = "柿木 勝之"
        self.user.address = "733-0011 広島県広島市西区横川町1-2-3 123"

    def test_名前を登録できる(self):
        self.assertEqual(self.user.name, "柿木 勝之")

    def test_住所を登録できる(self):
        self.assertEqual(self.user.address, "733-0011 広島県広島市西区横川町1-2-3 123")

class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        user = User()
        user.name = "柿木 勝之"
        user.address = "733-0011 広島県広島市西区横川町1-2-3 123"
        repo = Repository()
        repo.add_user(user)

        self.assertEqual(repo.get_user(0).name, "柿木 勝之")

class User:
    pass


class Repository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, index):
        return self.users[index]