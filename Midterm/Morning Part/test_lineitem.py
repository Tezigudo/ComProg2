from unittest import TestCase
from sale import *


class TestSales(TestCase):

    def setUp(self) -> None:
        self.sale = Sale()
        self.banana = Product('111', 'Banana', 0.99)
        self.apple = Product('222', 'Apple', 1.99)

    def test_init(self):
        """at initializea new Sale is empty and has a total price 0"""
        self.assertEqual(self.sale.all_product_id, [])
        self.assertEqual(self.sale.get_total(), 0)
        self.assertEquals(list(self.sale), [])

    def test_add_single_item(self):
        """if you add different quantities of a single product
        then the total sale price and quantity in the LineItem are always correct."""

        self.sale.add_item(self.banana, 3)
        self.sale.add_item(self.apple, 1)

        self.assertEqual(self.sale.all_product_id, ['111', '222'])
        self.assertAlmostEqual(self.sale.get_total(), 3.97, 4)
        self.assertEquals(str(list(self.sale)), str([LineItem(self.banana, 4), LineItem(self.apple, 1)]))

    def test_add_multiple_item(self):
        """adding 2 same thing together much merge into 1"""
        self.sale.add_item(self.banana, 3)
        self.sale.add_item(self.banana, 2)
        self.assertEqual(str(list(self.sale)), str([LineItem(self.banana, 5)]))

    def test_remove_some_quantity(self):
        """remove some item"""
        self.sale.add_item(self.apple, 5)
        self.sale.remove_item('222', 2)
        self.assertEqual(str(list(self.sale)), str([LineItem(self.apple, 3)]))

    def test_remove_all_quantity(self):
        """remove all item and must have nothing into the sale collection"""
        self.sale.add_item(self.banana, 5)
        self.sale.remove_item('111', 5)
        self.assertEqual(list(self.sale), [])
        self.assertEqual(self.sale.get_total(), 0)
