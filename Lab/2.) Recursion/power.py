def power(x: int, n: int) -> int:
    """Compute x raised to the power n, using recursion.

    Do not use Python's builtin syntax for computing powers.

    :param x: a number (int or float) to compute powers of
    :param n: a non-negative integer that is the power to compute
    :returns: x raised to the n-th power

    Examples:
    >>> power(2, 0)
    1
    >>> power(2, 1)
    2
    >>> power(2, 10)
    1024
    >>> power(10.0, 4)
    10000.0
    >>> power(0, 4)
    0
    >>> power(0, 0)
    1
    """
    # Basecase
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x, n-1)  # Recursive case
