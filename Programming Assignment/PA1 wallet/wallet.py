from copy import copy
from typing import List

from cash import *  # import everything from cash.py
from money import Money


class Wallet:
    """An electronic wallet holds cash that you can insert and withdraw.
    """

    def __init__(self):
        """Create an empty wallet."""
        self.items = []

    def __iter__(self):
        return iter(self.items)

    @property
    def currency_list(self) -> List[str]:
        """get the list of currencies in the wallet."""
        return [currency.currency for currency in self.items]

    def deposit(self, *items) -> None:
        """Deposit cash into the wallet.

        :param items: one or more Cash items to deposit.
        :raises TypeError: if any of the items is not Cash.
        :raises ValueError: if any of the items has non-positive value.
        """
        # check whether all items are Cash
        if any(not isinstance(cash, Cash) for cash in items):
            raise TypeError('cash must come from Cash object')
        # check whether all items have positive value
        if any(cash.value <= 0 for cash in items):
            raise ValueError('value must be non-positive value')
        # add the items to the wallet
        for cash in items:
            self.items.append(cash)

    def balance(self, currency: str) -> Money:
        """Return the balance of the wallet for a particular currency.

        It returns the total value of Money in the wallet having the
        requested currency (ignores any Money in other currencies).
        :param currency:  the currency to compute balance of
        :returns:  the total of Money in wallet having the requested currency.
        """
        # create a Money object with the currency
        now_money = Money(0, currency)
        for money in self.items:
            if money.currency == currency:
                now_money += money
        return now_money

    def is_empty(self) -> bool:
        """Test if there is anything in the wallet.

        :returns: True if there is nothing in the wallet, otherwise False
        """
        return not self.items

    def get_items(self) -> List[Money]:
        """Return a list of the shallow copy of items in the wallet.

        :returns: a shallow copy of the list of items in the wallet.
        """
        return copy(self.items)

    def exact_money(self, currency: str) -> List[Money]:
        """Return a list of cash items in the wallet having the requested currency.

        :param currency: the currency of the cash items to return
        :returns: a list of cash items in the wallet having the requested currency.
        """
        return [item for item in self.get_items() if item.currency == currency]

    def withdraw(self, amount: Money) -> List[Money]:
        """Withdraw cash from the wallet, so that the withdrawn amount
        has a value equal to amount, in the requested currency.

        :param amount: amount of Money to withdraw
        :returns: a list of cash items from the wallet whose total value
                equals the amount, and having the same currency as amount.
                Returns None if the withdraw cannot be performed.

        :raises ValueError: if amount.value is not positive
        :raises TypeError: if amount is not a Money object
        """
        # Hint:
        # 1. call a helper function to perform withdraw by recursion.
        #   the helper should not modify the list of items.
        # 2. when the helper function returns, if it returned a list
        #   of cash to withdraw, then remove those items from the cash
        #   list of this wallet.  Then return the stuff you withdraw.

        # check whether amount is a Money object
        if not isinstance(amount, Money):
            raise TypeError('amount must be a Money object')
        # check whether amount.value is positive
        if amount.value < 0:
            raise ValueError('amount must be non-negative value')

        # exact money which same currency as amount param
        exacted_item = self.exact_money(amount.currency)
        # call helper function to perform withdraw
        towithdraw = self.withdraw_from(amount, exacted_item)
        # It will return None if the withdraw cannot be performed.
        return towithdraw and [self.items.pop(self.items.index(val)) for val in towithdraw]

    @staticmethod
    def withdraw_from(amount: Money, items: List[Money], index=0) -> List[Money]:
        """Withdraw an amount from a list of Money (actually Cash) items.

        This is a helper method that decides what items (if any) should
        be withdrawn from the Wallet. It does not modify the parameters.

        :param amount: the amount of Money to withdraw
        :param items: a list of Cash items to choose from for withdraw.
        :returns: a list of elements from the items parameter with value
                equal to amount. Returns None if cannot perform the withdraw.


        note: each element in items in my example is a Cash object
        but I illustrate only value of each object.

        Ex. of this recursive method:
        amount.value = 30 and items = [10, 20, 30, 40]
        it will call itself with amount = 100, items = [50, 20, 10, 5, 1]
        first, amount: 100, items = [50, 20, 10, 5, 1], ind=0
                                     ^
        then, amount = 100-50, items = [50, 20, 10, 5, 1], ind=1
                                             ^
        amount = 50-20, items = [50, 20, 10, 5, 1], ind=2
                                          ^
        amount = 30-10, items = [50, 20, 10, 5, 1], ind=3
                                             ^
        amount = 20-5, items = [50, 20, 10, 5, 1], ind=4
                                               ^
        amount = 10-1, items = [50, 20, 10, 5, 1], ind=5
                                                ^
        amount = 9, items = [50, 20, 10, 5, 1], ind=6
        this case will return None because not enough money/index out of range


        """
        # the algorithm is like the groupsum recursion problem.
        # but you can only withdraw items with currency matching
        # the currency in `amount`.

        # Basecase
        # if the amount is zero, return an empty list
        if not (val := amount.value):
            return []
        # if there are no items or index out of range, return None
        if val < 0 or index == len(items):
            return None

        # Recursive case
        # it will call function itself with amount = amount.value - items[index].value
        # and items = items[index+1:]
        # if prev_recursion is None it mean that it must be a list and can sum untill zero
        # then append itself with prevcall.
        if (prev_call := Wallet.withdraw_from(amount-items[index], items, index+1)) is not None:
            return [items[index]] + prev_call

        # if prevcall is None It mean that It goes wring way
        # Do a backtrack!! (go to previous recursion call)
        return Wallet.withdraw_from(amount, items, index+1)
