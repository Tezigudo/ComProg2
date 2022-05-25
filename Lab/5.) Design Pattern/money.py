"""this is money.py"""


class Money:
    """Money represents a unit of value with a currency."""

    def __init__(self, value: float, currency: str):
        """Initialize a new Money object.

        Parameters:
            value:  the value of the money
            currency: the currency of the money

        Raises:
            ValueError if the currency is an empty string
            TypeError if value is not a number or currency is not a string
        """
        # check that value is a number
        if not isinstance(value, (int, float)):
            raise TypeError('value must be numeric')
        # check that currency is a string
        if not isinstance(currency, str):
            raise TypeError('currency must be a string')
        # this tests for both None and empty string
        if not currency:
            raise ValueError("currency must have a value")
        # assign the value and currency
        self._value = value
        self._currency = currency

    @property
    def value(self) -> float:
        """get a value of this money object.

        Returns:
            value of this money object
        """
        return self._value

    @property
    def currency(self) -> str:
        """Get the currency of this money object.

        Returns:
            the currency of this money object
        """
        return self._currency

    def __eq__(self, other: object) -> bool:
        """Two money objects are equal if they have the same value and currency.

        Parameters:
            other - a Money object to compare to this
        Returns:
            True if they have same value and currency, otherwise False
        """
        # check that other is a Money object
        if not isinstance(other, Money):
            return False
        return self.value == other.value and self.currency == other.currency

    def __ls__(self, other: object) -> bool:
        """Compare this money object to another, provided that the currencies are the same.

        Arguments:
            other - another money object to compare to this one

        Returns:
            True if this money object is less than other, False otherwise.

        Raises:
            ValueError if the currencies are not the same.
            TypeError if other is not an instance of Money or a subclass of Money.
        """
        # check that other is a Money object
        if isinstance(other, Money):
            # check that other has the same currency
            if self.currency != other.currency:
                raise ValueError('Money objects must have the same currency')
            return self.value < other.value
        # check that other is a number
        if isinstance(other, (int, float)):
            return self.value < other
        # if other is not a Money object or a number, raise TypeError
        raise TypeError(
            'cant operate with other objext except int float and Money')

    def __gt__(self, other: object) -> bool:
        """Compare this money object to another, provided that the currencies are the same.

        Arguments:
            other - another money object to compare to this one

        Returns:
            True if this money object is greater than other, False otherwise.

        Raises:
            ValueError if the currencies are not the same.
            TypeError if other is not an instance of Money or a subclass of Money.
        """
        # check that other is a Money object
        if isinstance(other, Money):
            # check that other has the same currency
            if self.currency != other.currency:
                raise ValueError('Money objects must have the same currency')
            return self.value > other.value
        # check that other is a number
        if isinstance(other, (int, float)):
            return self.value > other
        # if other is not a Money object or a number, raise TypeError
        raise TypeError(
            'cant operate with other objext except int float and Money')

    def __str__(self) -> str:
        """Return a string representation of this money object.
        if value is integer, return value and currency
        if value is float, return value and currency with 2 decimal places

        Returns:
            a string representation of this money object in the format
        """
        # check if value is an integer
        if isinstance(self.value, int):
            return f'{self.value:,} {self.currency}'
        return f'{self.value:,.2f} {self.currency}'
    __repr__ = __str__  # set __repr__ to __str__

    def __add__(self, other: object) -> object:
        """Add two money objects having the same currency.

        Arguments:
            other - another money object to add to this one
        Returns:
            the sum of this money and other other as a new Money object
        Raises:
            ValueError if the object have different currencies. """
        # check that other is a Money object
        if not isinstance(other, Money):
            raise TypeError('other must be a Money object')
        # check that other has the same currency
        if self.currency != other.currency:
            raise ValueError('Money objects must have the same currency')
        return Money(self.value + other.value, self.currency)

    def __sub__(self, other):
        """Subtract another money value (other) from this one, provided that the
        currencies are the same.

        Arguments:
            other: another Money object having the same currency as this one.
        Returns:
            a new Money object whose value is the difference between this and other.
            The value may be positive, zero, or negative.
        Raises:
            ValueError if the currencies are not the same.
            TypeError if other is not an instance of Money or a subclass of Money.
        """
        # check that other is a Money object
        if not isinstance(other, Money):
            raise TypeError('other must be a Money object')
        # check that other has the same currency
        if self.currency != other.currency:
            raise ValueError('Money objects must have the same currency')
        return Money(self.value - other.value, self.currency)

    def __mul__(self, other: object) -> object:
        """Multiply a money object by a number.

        Arguments:
            other - a number to multiply this money object by

        Returns:
            the product of this money object and other as a new Money object

        Raises:
            TypeError if other is not a number
        """
        # check that other is a number
        if not isinstance(other, (int, float)):
            raise TypeError('other must be numeric')
        return Money(self.value * other, self.currency)

    @classmethod
    def fromstring(cls, one_string: str) -> object:
        """Create a new Money object from a string.

        Arguments:
            one_string - a string in the format 'value currency'

        Returns:
            a new Money object with the value and currency extracted from the string

        Raises:
            ValueError if the string is not in the correct format
        """
        # split the string into value and currency
        parts = one_string.split()
        # check that there are exactly two parts
        if len(parts) != 2:
            raise ValueError('invalid format')
        value = float(parts[0])
        currency = parts[1]
        return cls(value, currency)
