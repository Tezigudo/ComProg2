## Factory Method Pattern

1. Read [factory method pattern](https://refactoring.guru/design-patterns/factory-method) on refactoring.guru.

2. Python Code Example: <https://en.wikipedia.org/wiki/Factory_method_pattern>

## 1. Answer these Questions in this README.

1. Describe the situation or context where you may want to use the Factory Method pattern. That is, in what kind of situation is it useful?

<u>Ans.</u> Suppose you have a class that creates objects of different types. You can use the Factory Method pattern to create objects of different types.

2. What is the benefit of using the Factory Method pattern, rather than just creating objects directly?

<u>Ans.</u> The benefit of using the Factory Method pattern is that you can create objects of different types.

3. In the `MoneyFactory` class, why is `get_instance` a class method rather than an instance method?

<u>Ans.</u> Because `get_instance` is a class method, it can be used to create objects of different types whatever, It can be use due a multiple object with one set.

## Implement Concrete MoneyFactories for Thai and Malaysian Money
****
Complete the code in `money_factory.py`.

The Malaysian currency is "Ringgit". Since 2012 Malaysian has had these denominations:
- Coins 0.0(), 0.10, 0.20, 0.50 Ringgit (colloquially 5, 10, 20, and 50 *sen*)
- Banknotes 1, 5, 10, 50, 100.  The 2 Ringgit banknote was discontinued in 2012, but some are still in circulation.  Since it's not made any more, the factory won't create it.
