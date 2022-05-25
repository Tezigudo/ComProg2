from product import Product


class LineItem:

    def __init__(self, product: Product, qnty: int):
        if not isinstance(product, Product):
            raise TypeError("Can only add products to a sale")
        self._product = product
        self.quantity = qnty

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        """get or set a quantity"""
        return self._quantity

    @quantity.setter
    def quantity(self, amount):
        if amount < 0:
            raise ValueError("Quantity must be zero or positive")
        if not isinstance(amount, int):
            raise TypeError("Quantity must be an integer")
        self._quantity = amount

    def get_price(self):
        return float(self.product.unit_price * self.quantity)

    def __eq__(self, other) -> bool:
        return self.product == other.product and self.quantity == other.quantity

    def __add__(self, other):
        if not isinstance(other, LineItem):
            raise TypeError("Can only add LineItem to LineItem")
        if self.product != other.product:
            raise ValueError("Cannot add LineItems with different products")
        # return LineItem(self.product, self.quantity + other.quantity)
        return type(self)(self.product, self.quantity + other.quantity)

    def __sub__(self, other):
        if not isinstance(other, LineItem):
            raise TypeError("Can only subtract LineItem from LineItem")
        if self.product != other.product:
            raise ValueError(
                "Cannot subtract LineItems with different products")
        # return LineItem(self.product, self.quantity - other.quantity)
        return type(self)(self.product, self.quantity - other.quantity)

    def __str__(self) -> str:
        return self.product.description
    __repr__ = __str__


class TwoForOneItem(LineItem):

    def get_price(self):
        free_quantity = self.quantity // 2
        quantity = self.quantity - free_quantity

        return float(self.product.unit_price * (quantity))

    def __str__(self) -> str:
        return super().__str__() + ["", " (2-for-1)"][self.quantity > 1]
    __repr__ = __str__
