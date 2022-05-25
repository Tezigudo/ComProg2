from types import NoneType
from typing import List
from longest_word import count

def tracer(func):
    """decorator that print evey time that finction was call"""
    count = 0  # number of times the function was called

    def print_func(*args, **kwargs):
        """print function name and arguments"""
        nonlocal count  # nonlocal variable
        # print the function name and arguments if any,
        # with indentation based on the call depth
        kw_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        if len(args) == 1:
            print('  ' * count + f"{func.__name__}(", *args, ') ', kw_str, sep='')
        else:
            print('  ' * count + f"{func.__name__}{args} {kw_str}")
        count += 1  # increment the call depth
        result = func(*args, **kwargs)  # call the function
        print('  ' * (count-1), result, sep='')  # print the result
        count -= 1  # decrement the call depth
        return result
    return print_func


@tracer
def groupsum_helper(arr: List[int], target: int, index: int) -> List[int] | NoneType:
    """ this is a helper function for groupsum

    Arguments:
        arr: the list of values
        target: the target value
        index: the index of the current value

    Returns:
        a list of values that sum to the target value
    """

    # base case
    # check whether the target is 0 or index is out of range
    if not target:  # return an empty list if target is 0
        return []

    # return None if index is out of range
    if index == count(arr) or target < 0:
        return None
    # recursive case
    # it will recursive with target minus the current value (it same as plus)
    # while the target is not 0 and index is not out of range
    if (rest_val := groupsum_helper(arr, target - arr[index], index + 1)) is not None:
        # when the recursive call returns a list, it will add the current value
        return [arr[index]] + rest_val
    # if cant find the solution, it will return None
    # then do a back tracking and it will check the next value
    return groupsum_helper(arr, target, index + 1)


def groupsum(target: int, values: List[int]) -> List[int]:
    """
    Choose a subset of integers from a list such that the sum equals a target.

    If there is no solution, return None. Do not modify the values parameter.

    :param target:  the desired sum of integers.  Must be non-negative.
    :param values:  a list of positive integers that can be chosen from to
                    find a subset whose sum equals target. Each element in
                    values can be used only once.
    :returns:       a list of integers from the values whose sum equals target,
                    or None if there is no solution.

    :raises:        AssertionErrir if target is negative.

    Examples:
    >>> groupsum(0, [1,2,3])    # easy! You don't have to add anything
    []
    >>> groupsum(2, [1,2,3])
    [2]
    >>> groupsum(8, [10,5,4,2,2]) # 8 = 4 + 2 + 2
    [4, 2, 2]
    >>> groupsum(7, [10,5,4,2,2])
    [5, 2]
    >>> groupsum(3, [10,5,4,2,2]) is None
    True
    >>> groupsum(25, [10,5,4,2]) is None
    True
    """
    assert target >= 0, "target value must be non-negative"
    return groupsum_helper(values, target, 0)

print(groupsum(25, [10,5,4,2]))
