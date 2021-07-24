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

class User:
    pass