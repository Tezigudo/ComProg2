import abc
from typing import List, Union

from cash import *


class MoneyFactory(abc.ABC):
    """Abstract base class for factory class that creates money."""

    # class variable for a single money factory
    # the same instance is returned every time get_instance is called.
    instance = None

    def __init__(self):
        # what are the values of coins and banknotes?
        self.currency: str = ''
        self.COINVALUE: List[Union[int, float]] = []
        self.BANKVALUE: List[int] = []

    def create_cash(self, value, currency=None) -> Cash:
        """Make cash in the default currency."""
        raise NotImplementedError("not implemented")

    @classmethod
    def get_instance(cls):
        """Get a singleton instance of the factory."""
        if not cls.instance:
            cls.instance = MalayMoneyFactory()
        return cls.instance

    @classmethod
    def set_factory(cls, factory):
        """Set the money factory instance to use."""
        cls.instance = factory


class MalayMoneyFactory(MoneyFactory):
    """Class for create Malay money"""

    def __init__(self):
        # values of coins and banknotes
        self.currency: str = "Ringgit"
        self.__COINVALUE: List[Union[int, float]] = [0.05, 0.10, 0.2, 0.5]
        self.__BANKVALUE: List[int] = [1, 5, 10, 50, 100]

    def create_cash(self, value) -> Cash:
        """Return a cash object of the requested value.

        :param value: a valid value for Malaysian currency.
        """
        if value in self.__COINVALUE:
            return Coin(value, self.currency)
        if value in self.__BANKVALUE:
            return Banknote(value, self.currency)
        raise ValueError(f"{value} is not valid for Malaysian currency")


class ThaiMoneyFactory(MoneyFactory):
    """Class for create Thai money """

    def __init__(self):
        super().__init__()
        # values of coins and banknotes
        self.currency: str = "Baht"
        self.__COINVALUE: List[Union[int, float]] = [0.25, 0.5, 1, 2, 5, 10]
        self.__BANKVALUE: List[int] = [20, 50, 100, 500, 1000]

    def create_cash(self, value) -> Cash:
        """Return a cash object of the requested value.

        :param value: a valid value for Thai currency.
        """
        if value in self.__COINVALUE:
            return Coin(value, self.currency)
        if value in self.__BANKVALUE:
            return Banknote(value, self.currency)
        raise ValueError(f"{value} is not valid for Thai currency")
