"""Collection of higher-order functions."""


def identity(*args):
    """The identity function returns its arguments.

    This is an ordinary function, not a higher-order function.
    :param *args: any number of positional arguments of any type

    Example:
    >>> identity("hello")
    'hello'
    >>> identity(2, 3, 4)
    (2, 3, 4)
    >>> identity()     # should be None
    """
    if not args:
        return None
    if len(args) == 1:
        return args[0]
    return args


def apply(f, iterable):
    """Apply a function to each item in an iterable object, and return the result.

    :param f: a function of one variable
    :param iterable: a collection or object that is iterable, meaning you can use
              it as the data source in a list comprehension [x for x in iterable].
    :returns: a list of f-values for items in the iterable.

    >>> from math import sqrt
    >>> it = [1, 4, 25, 36]
    >>> apply(sqrt, it)
    [1.0, 2.0, 5.0, 6.0]
    >>> apply(abs, range(-3, 3))
    [3, 2, 1, 0, 1, 2]
    """
    return list(map(f, iterable))


def inverse(f):
    """Return a function that is the reciprocal of f, that is, 1/f.

    >>> from math import sqrt
    >>> type(inverse(sqrt))
    <class 'function'>
    >>> inverse(sqrt)(4)
    0.5
    >>> inverse(sqrt)(25)
    0.2
    >>> inverse(sqrt)(0.0001)
    100.0
    >>> inverse(identity)(4)   # = 1/4
    0.25
    """
    return lambda x: 1/f(x)


def compose(f, g):
    """Create and return a function that is the composition of f and g.
    The function g should accept any number of parameters, so use the
    *args notation.
    You may need to handle the cases where *args is a single argument
    separately from multiple arguments.

    >>> from math import sqrt
    >>> f = compose(sqrt, abs)
    >>> type(f)
    <class 'function'>
    >>> f(-4)
    2.0
    >>> g = compose(sqrt, max)
    >>> g(25, -10, 100)
    10.0
    >>> g(-1, 0, -999)
    0.0
    """
    return lambda *args: f(g(*args))


def product(f, g):
    """Return a function that is the product of functions f and g.
    If h = product(f, g) then h(x) = f(x)*g(x).
    f and g are functions of a single parameter.

    >>> from math import sqrt
    >>> h = product(sqrt, identity)
    >>> h(4)
    8.0
    """
    return lambda *x: f(*x)*g(*x)


def polynomial(*coefs):
    """Return a polynomial function of one variable with coefficients
    given by the parameters. First parameter is the coefficient of the 
    higher power of "x".
    f = polynomial(3, 4)    returns linear func. f(x) = 3*x + 4
    g = polynomial(2, 5, 1) returns quadratic    g(x) = (2*x + 5)*x + 1
    h = polynomial(4)       returns              h(x) = 4
    k = polynomial(1,-2, 3,-4) returns  k(x) = ((x - 2)*x +3)*x - 4

    Note that writing (2*x + 5)*x + 1 is more efficient
    than the mathematically equivalent 2*x**2 + 5*x + 1,
    since you don't need to compute powers of x.

    >>> line = polynomial(3, 4)
    >>> line(0)
    4
    >>> line(10)
    34
    >>> cube = polynomial(2, 1, -3, 0)
    >>> cube(1)
    0
    >>> cube(10)
    2070
    >>> cube(-2)
    -6
    >>> polynomial(9)(5)
    9
    """
    def func(x):
        return sum(coefs[len(coefs) - i - 1]*x**i for i in range(len(coefs)))
    return func


if __name__ == '__main__':
    x = 5
    f = polynomial(9)
    print(f"f({x}) =", f(x))  # 9
    f = polynomial(1, 2, 3)
    print(f"f({x}) =", f(x))  # (5+2)*5 + 3 = 38
