import datetime

from money import Money


class Cash(Money):
    """Cash represents physical units of money, namely coins and banknotes."""

    def __init__(self, value: int, currency: str) -> None:
        """Initial a new cash object. The value must be positive.

        Raises:
            ValueError if the value is not a number or the currency is an empty string
        """
        if value <= 0:
            raise ValueError('value must be positive')
        super().__init__(value, currency)  # inherit all method from Money


class Coin(Cash):
    """Currency minted as coins, with a year."""

    def __init__(self, value: int, currency: str) -> None:
        """
        Initialize a new Coin object. The value must be positive.

        Arguments:
            year: the year the coin was minted
        """
        super().__init__(value, currency)  # inherit all method from Cash
        self.__year = datetime.date.today().year

    @property
    def year(self) -> int:
        """get the year the coin was minted.

        Returns:
            the year the banknote was minted
        """
        return self.__year

    def __str__(self) -> str:
        """Return a string representation of this money object.
        if value is integer, return value and currency
        if value is float, return value and currency with 2 decimal places

        Returns:
            a string representation of this Coin object in the format
        """
        return super().__str__() + ' Coin'
    __repr__ = __str__  # set __repr__ to __str__


class Banknote(Cash):
    """Currency in the form of paper money, with a year.

       The value of a Banknote must be a multiple of 10 units of currency.
    """

    def __init__(self, value: int, currency: str) -> None:
        """Initialize a new Banknote object.
        The value must be a multiple of 10 and have single digit

        Arguments:
            year: the year the banknote was minted
            serial_number: the serial number of the banknote

        Raises:
            ValueError if the value is not a multiple of 10 or the currency is an empty string
        """
        # inherit all method from Cash
        super().__init__(value, currency)
        if not self.valid_bank(value):
            raise ValueError(
                'must be a power of 10 and a single digit EX. 10, 20, 50, 100, 500, 1000, 4000')
        self.__year = datetime.date.today().year
        self._serial_number = str(id(self))

    @staticmethod
    def valid_bank(value: int) -> bool:
        """Check if the value is a multiple of 1

        Arguments:
            value: the value of the banknote

        Returns:
            True if value are multiple of 1 (not float int only)
        """

        return isinstance(value, int)

    @property
    def year(self) -> int:
        """get the year the banknote was minted.

        Returns:
            the year the banknote was minted
        """
        return self.__year

    @property
    def serial_number(self) -> str:
        """ Get the serial number of the banknote."""
        return self._serial_number

    def __str__(self) -> str:
        """Return a string representation of this money object.
        if value is integer, return value and currency
        if value is float, return value and currency with 2 decimal places

        Returns:
            a string representation of this Banknote object in the format
        """
        return super().__str__() + ' Banknote'
    __repr__ = __str__  # set __repr__ to __str__
