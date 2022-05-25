from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """Product is a kind of item for sale with id, description, and a unit price."""

    # attributes of a product, with "get" properties (auto-generated)
    product_id: str
    description: str
    unit_price: float

    # auto-generated constructor: 
    # __init__(self, product_id, description, unit_price)

    def __str__(self):
        return self.description
    
    def __repr__(self):
        name = type(self).__name__
        return f"{name}('{self.product_id}', '{self.description}', {self.unit_price})"
