"""
This is test for Backaccount.py
"""

import unittest

from bank_account import BankAccount, TransactionError


class BankAccountTest(unittest.TestCase):
    """ This is test for Bankaccount class"""

    def setUp(self):
        """Set up"""
        self.account = BankAccount("12345", "Tonwan")

    def test_new_account(self):
        """A new bank account must have balance 0"""
        balance = self.account.get_balance()
        self.assertEqual(0, balance)

    def test_deposit(self):
        """After deposit, the balance must be updated"""
        self.account.deposit(100)
        self.assertEqual(100, self.account.get_balance())

    def test_neg_deposit(self):
        """Deposit must be positive amount"""
        amounts = [0, -1, -100]
        for amount in amounts:
            with self.assertRaises(ValueError):
                self.account.deposit(amount)

    def test_deposit_and_withdraw_same_amount(self):
        """" After deposit and withdraw some part of it
        , the balance must be updated"""
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(50, self.account.get_balance())

    def test_deposit_then_withdraw_all_balance(self):
        """After deposit and withdraw all balance,
        the balance must be 0"""
        self.account.deposit(200)
        now_money = self.account.get_balance()
        self.account.withdraw(now_money)
        balance = self.account.get_balance()
        self.assertEqual(0, balance)

    def test_zero_balance_withdraw(self):
        """Withdraw when amount > balance"""
        with self.assertRaises(TransactionError):
            self.account.withdraw(100)


if __name__ == '__main__':
    unittest.main()
