import unittest


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User(name="高木 ブー", address="733-0000 広島県広島市西区横川町1-2-3")

    def test_名前を登録できる(self):
        self.assertEqual(self.user.name, "高木 ブー")

    def test_住所を登録できる(self):
        self.assertEqual(self.user.address, "733-0000 広島県広島市西区横川町1-2-3")


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
