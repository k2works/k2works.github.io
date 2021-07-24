import unittest

class TestUser(unittest.TestCase):
    def test_名前を登録できる(self):
        user = User()
        user.name = "test"
        self.assertEqual(user.name, "test")

class User:
    pass