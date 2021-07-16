import unittest


class TestUser(unittest.TestCase):
    def test_名前を登録できる(self):
        user = User(name='ユーザ名')
        self.assertEqual(user.name, 'ユーザ名')

    def test_住所を登録できる(self):
        user = User(name='ユーザー名', zip='123-4567', address='住所')
        self.assertEqual(user.zip, '123-4567')
        self.assertEqual(user.address, '住所')


class User:
    def __init__(self, name, zip=None, address=None) -> None:
        self.__name = name
        self.__zip = zip
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def zip(self):
        return self.__zip

    @property
    def address(self):
        return self.__address


unittest.main(argv=[''], verbosity=2, exit=False)
