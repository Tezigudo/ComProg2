"""
This module contain BankAccount class which
"""


import datetime
from typing import List, Union
from copy import deepcopy


class Transaction:
    """ Information about a transaction. """

    def __init__(self, types: str, amount: Union[int, float]) -> None:
        """ Initialize a transaction.

        Arguments:
            types {str} -- type of the transaction
            amount {int | float} -- amount of the transaction
        """
        self._types: str = types
        self._amount: Union[int, float] = amount
        self.date: datetime.datetime = datetime.datetime.now()

    @property
    def amount(self) -> Union[int, float]:
        """get the amount of this transaction"""
        return self._amount

    @property
    def types(self) -> str:
        """get the type of this transaction"""
        return self._types

    def __repr__(self) -> str:
        """return the string representation of this transaction"""
        return f"{self.date} {self.types} {self.amount}"
    __str__ = __repr__


class TransactionError(BaseException):
    """Exception class for transaction errors"""
    # marker class


class BankAccount:
    """A bank account with account id and owner.
       Transactions are recorded individually
    """

    def __init__(self, ids: str, owner: str) -> None:
        """
        Arguments:
            ids {str} -- account
            owner {str} -- owner of the account
        """
        self.ids: str = ids
        self.own: str = owner
        self.transactions: List[Transaction] = []

    def deposit(self, amount: Union[int, float]) -> None:
        """deposit to the bank account

        Argument:
            amount {int | float} -- amount to deposit

        Raises:
            ValueError: if amount is negative
        """
        if amount <= 0:
            raise ValueError("Deposit must be positive amount")
        transaction = Transaction("deposit", amount)
        self.transactions.append(transaction)

    def withdraw(self, amount: Union[int, float]) -> None:
        """Withdraw money from the bank account.

        Argument:
            amount {int | float} -- amount to withdraw

        Raises:
            ValueError: if amount is negative
            TransactionError: if amount is greater than the balance
        """
        if amounjjt <= 0:
            raise ValueError("Withdraw amount must be positive")
        balance = self.get_balance()
        if amount > balance:
            raise TransactionError(f"Insufficient funds to withdraw {amount}")
        transaction = Transaction("withdraw", -amount)
        self.transactions.append(transaction)

    def get_balance(self) -> Union[int, float]:
        """ Return the balance of the bank account.

        Returns:
            int | float -- the balance of the bank account
        """
        return sum(t.amount for t in self.transactions)

    def get_transactions(self) -> List[Transaction]:
        """ Return the list of transactions.

        Returns:
            List[Transaction] -- the list of transactions
        """
        return deepcopy(self.transactions)

    def __repr__(self) -> str:
        return f'{self.own} {self.get_balance()}'
