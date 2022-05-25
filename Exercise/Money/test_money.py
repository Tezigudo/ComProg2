"""A unittest for the Money class.

To run these tests at the command line, enter:
   python3 -m unittest test_money.py
or python3 test_money.py
"""
import unittest
from money import Money


class MoneyTest(unittest.TestCase):

    def test_constructor(self):
        """Constructor should raise ValueError if currency is missing."""
        with self.assertRaises(ValueError):
            m1 = Money(10, "")
        # this case is ambiguous. Accept either exception.
        with self.assertRaises((ValueError, TypeError)):
            m2 = Money(10, None)
        # legal usage, should not raise exception
        m1 = Money(0, "Baht")
        m2 = Money(0.01, "Cats")
        m3 = Money(-1, "Doge")
        m4 = Money(1000000000, "ZMB")

    def test_str_int_values(self):
        """__str__ should format int values as integers."""
        # int value, should not display a decimal part
        m1 = Money(20, "Baht")
        self.assertEqual("20 Baht", str(m1))
        # big int value, should include a comma
        m2 = Money(1234567, "Doge")
        self.assertEqual("1,234,567 Doge", str(m2))

    def test_str_float_values(self):
        """__str__ should format float values with 2 decimal places."""
        # non-int value should display 2 decimal places
        m1 = Money(0.5, "Ringgit")
        self.assertEqual("0.50 Ringgit", str(m1))
        # only show 2 decimal places
        m2 = Money(0.019, "Baht")
        self.assertEqual("0.02 Baht", str(m2))
        m3 = Money(1234567000.55, "USD")
        self.assertEqual("1,234,567,000.55 USD", str(m3))

    def test_eq(self):
        """Two money objects are equal only if value & currency are same."""
        self.assertEqual(Money(5, "Baht"), Money(5, "Baht"))
        # comparison should not depend on the type of value
        self.assertEqual(Money(5, "Baht"), Money(5.0, "Baht"))
        # some non-equal cases
        self.assertNotEqual(Money(5, "Baht"), Money(4.9999, "Baht"))
        self.assertNotEqual(Money(5, "Baht"), Money(5, "Bath"))
        self.assertNotEqual(Money(5, "Baht"), Money(5, "Doge"))

    def test_value_is_readonly(self):
        """The value should be a read-only property."""
        m1 = Money(20, "Baht")
        self.assertEqual(20, m1.value)
        with self.assertRaises(AttributeError):
            m1.value = 50
        # this test should never be reached
        self.assertEqual(20, m1.value)

    def test_currency_is_readonly(self):
        """The currency should be a read-only property."""
        m1 = Money(20, "USD")
        self.assertEqual("USD", m1.currency)
        with self.assertRaises(AttributeError):
            m1.currency = "Rupie"
        # this test should never be reached
        self.assertEqual("USD", m1.currency)

    def test_addition(self):
        """Can add money if and only if the currencies are same."""
        m1 = Money(9, "Baht")
        m2 = Money(1, "Baht")
        self.assertEqual(Money(10, "Baht"), m1+m2)
        # add should NOT alter the parameters
        self.assertEqual(9, m1.value)
        self.assertEqual(1, m2.value)
        # should not allow cross-currency addition
        with self.assertRaises(ValueError):
            bogus = Money(9, "Baht") + Money(1, "Doge")

    def test_multiply(self):
        """Can multiply money * float."""
        m1 = Money(10, "Baht")
        self.assertEqual(Money(15, "Baht"), m1 * 1.5)
        self.assertEqual(Money(50, "Baht"), m1 * 5)
        # multiply should NOT alter the parameters
        self.assertEqual(10, m1.value)
        # should not allow money * money
        with self.assertRaises(TypeError):
            bogus = Money(10, "Baht") * Money(1.5, "Baht")

    def test_fromstring(self):
        """fromstring class method creates a Money object from a string."""
        m1 = Money.fromstring("123 Doge-coin")
        self.assertIsInstance(m1, Money)
        self.assertEqual(123, m1.value)
        self.assertEqual("Doge-coin", m1.currency)
        m2 = Money.fromstring("2.345 Bananas")
        self.assertIsInstance(m2, Money)
        self.assertEqual(2.345, m2.value)
        self.assertEqual("Bananas", m2.currency)


if __name__ == '__main__':
    unittest.main(verbosity=2)
