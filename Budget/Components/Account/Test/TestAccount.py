import datetime as dt
import unittest

from Budget.Components.Account.Src.Account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()


    def testDepositAndWithdraw(self):
        amount = 2000.0
        date = dt.date(2021, 12, 4)
        description = "Swish"

        self.account.deposit(amount, date, description)
        self.assertEqual(self.account.balance(), amount)
        self.assertEqual(len(self.account.get_history()), 1)

        self.account.withdraw(amount, date, description)
        self.assertEqual(self.account.balance(), 0)
        self.assertEqual(len(self.account.get_history()), 2)

if __name__ == "__main__":
    unittest.main()
