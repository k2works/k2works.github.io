import unittest

class TestUser(unittest.TestCase):
    def test_名前を登録できる(self):
        user = User()
        user.name = "柿木 勝之"
        self.assertEqual(user.name, "柿木 勝之")

    def test_住所を登録できる(self):
        user = User()
        user.address = "733-0011 広島県広島市西区横川町1-2-3 123"
        self.assertEqual(user.address, "733-0011 広島県広島市西区横川町1-2-3 123")

class User:
    pass