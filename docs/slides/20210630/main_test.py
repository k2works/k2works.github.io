
import unittest
import hashlib


class Money:
    def __init__(self, amount, currency) -> None:
        self.__amount = amount
        self.__currency = currency

    def __str__(self) -> str:
        if self.__currency == 'JPY':
            return f'¥{self.__amount}'
        elif self.__currency == 'USD':
            return f'${self.__amount}'
        else:
            return f'{self.__amount}'

    def __eq__(self, other: object) -> bool:
        return(self.__amount == other.__amount and self.__currency == other.__currency)

    def __hash__(self) -> int:
        encoded_currency = int(hashlib.sha256(
            self.__currency.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        return hash(self.__amount + encoded_currency)

    def add(self, other: object) -> object:
        return Money(self.__amount + other.__amount, self.__currency)


class TestMoney(unittest.TestCase):
    def setUp(self) -> None:
        self.千円 = Money(1000, 'JPY')
        self.一万円 = Money(10000, 'JPY')
        self.千ドル = Money(1000, 'USD')

    def test_金額を表示する(self):
        self.assertEqual(str(self.千円), '¥1000')
        self.assertEqual(str(self.一万円), '¥10000')

    def test_外貨金額を表示する(self):
        self.assertEqual(str(self.千ドル), '$1000')

    def test_金額は等しい(self):
        self.assertEqual(self.千円, Money(1000, 'JPY'))
        self.assertNotEqual(self.千円, self.千ドル)

    def test_通貨を保持している(self):
        財布 = {self.千円}
        self.assertTrue(self.千円 in 財布)
        self.assertFalse(self.千ドル in 財布)

    def test_金額を合計する(self):
        二千円 = self.千円.add(Money(1000, 'JPY'))
        self.assertEqual(str(二千円), '¥2000')
        with self.assertRaises(ValueError, msg='異なる通貨では計算できません'):
            self.千ドル.add(Money(1000, 'JPY'))



unittest.main(argv=[''], verbosity=2, exit=False)
