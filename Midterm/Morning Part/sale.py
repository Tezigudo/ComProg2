from typing import Iterable

from lineitem import LineItem, TwoForOneItem
from product import Product
from store import Store


class Sale:
    def __init__(self):
        self.__items = {}

    def add_item(self, product: Product, quantity: int):
        # BUG: add items doesnt work
        # TODO: after finished unittest fixed this bug
        if not isinstance(product, Product):
            raise TypeError("Can only add products to a sale")
        if quantity < 0:
            raise ValueError("Quantity must be zero or positive")
        line = LineItem
        if Store.is_sale_item(product):
            line = TwoForOneItem

        if product.product_id not in self.__items:
            self.__items[product.product_id] = line(product, quantity)
        else:
            self.__items[product.product_id] += line(product, quantity)

    def remove_item(self, product_id, quantity):
        if product_id not in self.all_product_id:
            raise ValueError("product id must be in sale")
        other_line_item = LineItem(self.__items[product_id].product, quantity)
        if quantity < self.__items[product_id].quantity:
            self.__items[product_id] -= other_line_item
        elif quantity == self.__items[product_id].quantity:
            del self.__items[product_id]
        else:
            raise ValueError(
                "quantity must be less than or equal to the quantity of the product")

    def get_total(self):
        return sum(product.get_price() for product in self)

    @property
    def all_product_id(self):
        return list(self.__items.keys())

    def __iter__(self) -> Iterable[LineItem]:
        return iter(self.__items.values())
