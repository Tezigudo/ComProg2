"""Part 2: Define novel functions as a single statement."""
from math import sqrt
from typing import Union

from funclib import *

# problem 1
f = polynomial(1, 2, 6, 0, -10)

# problem 2
g = compose(polynomial(1, 2, -1), inverse(polynomial(1, 0, 1)))

# problem 3
h = product(identity, compose(sqrt, compose(polynomial(1, 1), abs)))


def round_to_4(n: Union[int, float]) -> float:
    return round(n, 4)


def real_f(x: Union[int, float]) -> float:
    """real value of f(X)"""
    return (x ** 4) + 2 * (x ** 3) + 6 * (x ** 2) - 10


def real_g(x: Union[int, float]) -> float:
    """real value of g(X)"""
    return 1/(x ** 2 + 1) ** 2 + 2 * (1 / (x ** 2 + 1)) - 1


def real_h(x: Union[int, float]) -> float:
    """real value of h(X)"""
    return x * sqrt(abs(x) + 1)


def doctests():
    """Examples of using the functions above.
    >>> all(round_to_4(f(x)) == round_to_4(real_f(x)) for x in range(-10, 10))
    True
    >>> all(round_to_4(g(x)) == round_to_4(real_g(x)) for x in range(-10, 10))
    True
    >>> all(round_to_4(h(x)) == round_to_4(real_h(x)) for x in range(-10, 10))
    True

    """
    # Don't copy and paste these observed values into your doctests.
    # Doctests should use known correct results (verify by manual computation).
    for x in [0, 1, 2]:
        print(f"f({x}) =", f(x))
    for x in [0, 1, -3]:
        print(f"g({x}) =", g(x))
    for x in [0, 1]:
        print(f"h({x}) =", h(x))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
