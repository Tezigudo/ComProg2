from sale import *
from store import *
from main import *


store = Store.get_instance()
sale = Sale()
water = store.get_product('101')
sale.add_item(water, 3)
p1 = store.get_product('111')
p2 = store.get_product('112')
sale.add_item(p1, 1)
sale.add_item(p2, 2)
sale.get_total()  # 95
sale.remove_item('112', 2)
sale.add_item(p1, 3)

print_sale(sale)
