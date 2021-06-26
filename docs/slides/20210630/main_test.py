
import unittest

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
        return(self.__amount == other.__amount)

class TestMoney(unittest.TestCase):
    def test_金額を表示する(self):
        千円 = Money(1000, 'JPY')
        一万円 = Money(10000, 'JPY')
        self.assertEqual(str(千円), '¥1000')
        self.assertEqual(str(一万円), '¥10000')

    def test_外貨金額を表示する(self):
        千ドル = Money(1000, 'USD')
        self.assertEqual(str(千ドル), '$1000')

    def test_金額は等しい(self):
        千円 = Money(1000, 'JPY')
        千ドル = Money(1000, 'USD')
        self.assertEqual(千円, Money(1000, 'JPY'))
        self.assertNotEqual(千円, 千ドル)


unittest.main(argv=[''], verbosity=2, exit=False)
