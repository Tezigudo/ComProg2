"""Tests of Cash, Coin, and Banknote"""
import re
import unittest
import datetime
from cash import *
# Money should already be imported (in cash), but protect against unusual code
from money import Money


class CoinTest(unittest.TestCase):

    def test_coin_is_cash(self):
        """Coin is a kind of Cash and Money, but not a Banknote."""
        c = Coin(1, "Baht")
        self.assertIsInstance(c, Cash)
        self.assertIsInstance(c, Money)
        self.assertNotIsInstance(c, Banknote)

    def test_coin_has_year(self):
        """Coin has a year property that is the year minted."""
        c = Coin(5, "Ringgit")
        year = datetime.date.today().year
        self.assertEqual(year, c.year)

    def test_coin_year_is_readonly(self):
        """Year is readonly property."""
        c = Coin(5, "Baht")
        with self.assertRaises(AttributeError):
            c.year = 2000

    def test_coin_has_positive_value(self):
        """Constructor should not allow non-positive values."""
        for value in [0, -0.5, -1, -10]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    c = Coin(value, "Ringgit")

    def test_coin_must_have_currency(self):
        """Coin must have a non-empty string currency."""
        with self.assertRaises(ValueError):
            c = Coin(5, "")

    def test_add_returns_money(self):
        """You can add cash, but the result is Money not Cash."""
        result = Coin(5, "Baht") + Coin(10, "Baht")
        self.assertIsInstance(result, Money)
        self.assertNotIsInstance(
            result, Coin, "Result of cash+cash should be Money")
        self.assertEqual(15, result.value)
        self.assertEqual("Baht", result.currency)

    def test_add_coin_and_money(self):
        """You can add coin and money. The result is Money (not Coin)."""
        for (value1, value2, sum_value) in [(1, -1, 0), (5, 0, 5), (10, -4, 6)]:
            with self.subTest(coin_value=value1, money_value=value2, sum_value=sum_value):
                result = Coin(value1, "Baht") + Money(value2, "Baht")
                self.assertIsInstance(result, Money)
                self.assertNotIsInstance(
                    result, Coin, "Result of cash+cash should be Money")
                self.assertEqual(sum_value, result.value)
                # try adding in opposite order
                result2 = Money(value2, "Baht") + Coin(value1, "Baht")
                self.assertIsInstance(result2, Money)
                self.assertEqual(result, result2)


class BanknoteTest(unittest.TestCase):

    def test_banknote_is_cash(self):
        """Banknote is a kind of Cash and Money, but not a Coin."""
        c = Banknote(100, "Baht")
        self.assertIsInstance(c, Cash)
        self.assertIsInstance(c, Money)
        self.assertNotIsInstance(c, Coin)

    def test_banknote_has_year(self):
        """Banknote has a year property that is the year minted."""
        c = Banknote(100, "Ringgit")
        year = datetime.date.today().year
        self.assertEqual(year, c.year)

    def test_banknote_year_is_readonly(self):
        """Year is readonly property."""
        c = Banknote(100, "Baht")
        with self.assertRaises(AttributeError):
            c.year = 2000

    def test_banknote_has_positive_value(self):
        """Constructor should not allow non-positive values."""
        for value in [0, -10, -50, -100]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    c = Banknote(value, "Ringgit")

    def test_banknote_disallows_weird_values(self):
        """Banknotes don't have decimal (1.5) or weird values(7)."""
        for value in [0.5, 10.5, 7, 1000.5]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    banknote = Banknote(value, "Ringgit")

    def test_banknote_must_have_currency(self):
        """Banknote must have a non-empty string currency."""
        with self.assertRaises(ValueError):
            c = Banknote(100, "")

    def test_add_returns_money(self):
        """You can add cash, but the result is Money not Cash."""
        result = Banknote(50, "Baht") + Banknote(10, "Baht")
        self.assertIsInstance(result, Money)
        self.assertNotIsInstance(
            result, Banknote, "Result of cash+cash should be Money")
        self.assertEqual(60, result.value)
        self.assertEqual("Baht", result.currency)

    def test_add_banknote_and_money(self):
        """You can add banknote and money. The result is Money (not Banknote)."""
        for (value1, value2, sum_value) in [(100, -100, 0), (500, 0, 500), (100, -40, 60)]:
            with self.subTest(banknote_value=value1, money_value=value2, sum_value=sum_value):
                result = Banknote(value1, "Baht") + Money(value2, "Baht")
                self.assertIsInstance(result, Money)
                self.assertNotIsInstance(
                    result, Banknote, "Result of cash+cash should be Money")
                self.assertEqual(sum_value, result.value)
                # try adding in opposite order
                result2 = Money(value2, "Baht") + Banknote(value1, "Baht")
                self.assertIsInstance(result2, Money)
                self.assertEqual(result, result2)
