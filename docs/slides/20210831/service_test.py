import unittest
from enum import Enum


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('Alice', 'password', Role.管理者)

    def test_名前を登録できる(self):
        self.assertEqual(self.user.name, 'Alice')

    def test_パスワードを登録できる(self):
        self.assertEqual(self.user.password, 'password')

    def test_権限を登録できる(self):
        self.assertEqual(self.user.role, Role.管理者)


class TestService(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('Alice', 'password')
        self.applicationService = ApplicationService()
        self.domainService = DomainService(self.applicationService)

    def test_ユーザを登録できる(self):
        self.applicationService.save(self.user)
        user = self.applicationService.get(self.user)
        self.assertEqual(user.name, 'Alice')

    def test_すでにユーザが登録されているか確認できる(self):
        self.applicationService.save(self.user)
        with self.assertRaises(ValueError, msg='ユーザはすでに登録されています'):
            self.domainService.check(self.user)


class TestRepository(unittest.TestCase):
    def test_ユーザを登録できる(self):
        repository = Repository()
        repository.register(User('Alice', 'password', Role.管理者))
        user = repository.find_by_name('Alice')
        self.assertEqual(user.name, 'Alice')


class Role(Enum):
    管理者 = 1
    利用者 = 2


class User:
    def __init__(self, name: str, password: str, role: Role = Role.利用者) -> None:
        self.name = name
        self.password = password
        self.role = role


class DomainService:
    def __init__(self, service) -> None:
        self.service = service

    def check(self, user: User):
        check_user = self.service.get(user)
        if check_user is not None:
            raise ValueError('ユーザはすでに登録されています')


class ApplicationService:
    def __init__(self) -> None:
        self.repository = Repository()

    def save(self, user: User):
        self.repository.register(user)

    def get(self, user: User) -> User:
        return self.repository.find_by_name(user.name)


class Repository:
    def __init__(self) -> None:
        self.users = []

    def register(self, user: User) -> None:
        self.users.append(user)

    def find_by_name(self, name: str):
        for user in self.users:
            if user.name == name:
                return user
