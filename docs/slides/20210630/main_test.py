
import unittest


class TestMoney(unittest.TestCase):
    def test_金額を表示する(self):
        千円 = Money(1000, 'JPY')
        self.assertEqual(str(千円), '¥1000')


unittest.main(argv=[''], verbosity=2, exit=False)
