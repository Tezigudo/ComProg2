from money_factory import *
MoneyFactory.set_factory(ThaiMoneyFactory())
assert isinstance(MoneyFactory.get_instance(), ThaiMoneyFactory), "ThaiMoneyFactory is not set"
assert MoneyFactory.get_instance().create_cash(10) == Coin(10, "Baht"), "ThaiMoneyFactory is not object"
