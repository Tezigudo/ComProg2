from product import Product


class Store:
    """A Store manages a collection of products.

    Store is a singleton. To get the store you should use:
    store = Store.get_instance()
    """
    PRODUCTS_FILE = "products.txt"
    # fruit is on sale
    SALE_ITEMS = ["110", "111"]

    # a single instance of the store
    instance = None

    def __init__(self):
        """initialize the store be reading the product data
        and creating products."""
        self.products = {}
        self.load_products(self.PRODUCTS_FILE)

    @classmethod
    def get_instance(cls):
        if Store.instance == None:
            Store.instance = Store()
        return cls.instance

    def load_products(self, filename):
        """Create products from a data file."""
        try:
            file = open(filename)
        except IOError as e:
            print(f"Could not open data file {filename}")
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'): continue
            try:
                (pid, desc, price) = line.split(',')
                self.products[pid] = Product(pid, desc, float(price))
            except Exception:
                print(f"Invalid product data: {line}")
        file.close()

    def get_product(self, product_id: str) -> Product:
        """Get a product by it's product id."""
        if product_id in self.products:
            return self.products[product_id]
        raise ValueError(f"No product with id {product_id}")

    def get_products(self):
        """Get a list of all products in the store."""
        return list(self.products.values())

    @classmethod
    def is_sale_item(cls, product):
        """Returns True if the product is on sale with 2-for-1 pricing.

        :param product: a Product or a product_id to test if on sale
        :returns: True if the product is on sale 2-for-1
        """
        pid = product.product_id if isinstance(product, Product) else product
        return pid in cls.SALE_ITEMS
