from typing import List


def fibonacci2(n: int) -> List[int]:
    """Helper function for fibonacci.

    that return 2 most recent fibonacci number
    require 1 recursive call( O(N) )

    Arguments:
        n: the index of the fibonacci number

    Returns:
        a list of 2 most recent fibonacci numbers

    ex.
    fibonacci2(0) -> [0, 0]
    fibonacci2(1) -> [0, 1]
    fibonacci2(2) -> [1, 1]
    """
    # Base case
    if n < 1:
        return [0, 0]
    if n == 1:
        return [0, 1]
    fib = fibonacci2(n - 1)  # recursive case
    return [fib[1], fib[0] + fib[1]]


def fibonacci(n: int) -> int:
    """Smart recursive Fibonacci calculator.

    Use recursion and a HELPER FUNCTION to compute fibonacci numbers
    in a way that makes recursive computation blazingly fast.
    The usual recursive fibonacci is sloooooooooow due to the
    duplicate recursive computation.

    The usual recursive solution is (as in the starter code):
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    Each term on the right hand side will in turn result in 2 more
    calls to the fibonacci function, so you get an explosion in the
    number of recursive calls.
    fibonacci(2) - 2 recursive calls
    fibonacci(3) - 2 + 1 recursive calls
    fibonacci(4) - 3 + 2 recursive calls
    fibonacci(5) - 5 + 3 recursive calls

    Try it yourself!
    Run this file and try to compute the first 40 fibonacci numbers.

    Write a HELPER function named fibonacci2 defined as follows:
    fibonacci2(0) -> [0, 0]
    fibonacci2(1) -> [0, 1]
    fibonacci2(2) -> [1, 1]

    at each step, fibonacci2(n) returns the 2 most recent fibonacci numbers.
    This should require ONLY ONE recursive function call,
    i.e. fibonacci2(n) calls fibonacci2(n-1) one time and
    uses the result to compute its own result.

    Then, in the fibonacci function, simply call the helper
    function and return only the 2nd element in the result.
    Only the helper function performs recursion.

    If you get it right, computing even large fibonacci
    numbers will be blazingly fast.
    Examples:
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    >>> fibonacci(25)
    75025
    >>> fibonacci(32)        # this may be a bit slow
    2178309
    """
    # The naive approach
    # if n < 1:
    #     return 0
    # if n == 1:
    #     return 1
    # return fibonacci(n-1) + fibonacci(n-2)

    #  using helper fib
    return fibonacci2(n)[1]


if __name__ == '__main__':
    print("Compute fibonacci(n) for n = 1, ..., limit.")
    limit = int(input("Max value of n to compute fibonacci(n)? "))
    for n in range(1, limit+1):
        print(f"fibonacci({n}) = ", end="")
        print(fibonacci(n))
