def tribonacci(n: int) -> int:
    """Return the n-th Tribonacci number.

    A tribonacci number is defined as the sum of 3 previous Tribonacci
    numbers, similar to the way Fibonacci's are the sum of the previous
    two Fibonacci numbers.  The sequence is defined as:

    tribonacci(n) = 0 for n < 1
    tribonacci(1) = 1
    tribonacci(2) = 1
    tribonacci(3) = tribonacci(2) + tribonacci(1) + tribonacci(0)
    tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

    No not use a loop or list or attempt to store prior Tribonacci values.
    Use pure recursion, even though its terribly inefficient.

    :param n: a non-negative integer that is the tribonacci value to return

    Examples:
    >>> tribonacci(0)
    0
    >>> tribonacci(1)
    1
    >>> tribonacci(2)
    1
    >>> tribonacci(3)
    2
    >>> tribonacci(4)
    4
    >>> tribonacci(5)
    7
    >>> tribonacci(20)
    66012
    """
    # Base case
    if n < 1:
        return 0
    if n < 3:
        return 1
    # Recursive case
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


if __name__ == '__main__':
    limit = int(input("upper limit on Tribonaccis: "))
    for n in range(1, limit+1):
        print(f"Tribonacci({n}) = {tribonacci(n)}")
