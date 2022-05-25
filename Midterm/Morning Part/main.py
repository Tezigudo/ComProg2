from store import Store
from sale import Sale


def print_sale(sale: Sale):
    """Print a nicely formatted sale report."""

    print(f'{"ID":<6}{"Description":<21}{"Qnty":<9}{"Price":<6}')
    for lineitem in sale:
        product = lineitem.product
        print(f'{product.product_id:<6}{product.description:<21}{lineitem.quantity:<9}{lineitem.get_price():<6}')
    print(f'{"Total":>10}{sale.get_total():>30}')


def demo():
    sale = Sale()
    store = Store.get_instance()
    items = [('101', 2),
             ('108', 3),
             ('110', 2),
             ('120', 1),
             ('110', 2),
             ('108', -2)]
    for (product_id, qnty) in items:
        product = store.get_product(product_id)
        if qnty > 0:
            # buy some quantity of a product
            print(f"Buy {qnty} of {str(product)}")
            sale.add_item(product, qnty)
        elif qnty < 0:
            # reduce some quantity of a product already in the sale
            print(f"Remove {-qnty} of {str(product)}")
            sale.remove_item(product_id, -qnty)

    print("Sale contains")
    print_sale(sale)


if __name__ == '__main__':
    demo()
