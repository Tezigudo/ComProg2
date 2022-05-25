from typing import List
from longest_word import count


def sum_list(arr: List[int]) -> int:
    """Return the sum of the values in the list.

    Arguments:
        arr {List[int]} -- list of numbers to sum.

    Returns:
        int -- sum of the values in the list.
    """

    if not arr:  # check whether the list is empty
        return 0
    # return the first element in the list plus the sum of the rest of the list
    return arr.pop() + sum_list(arr)


def split_array2(arr: List[int], index=1) -> bool:
    """ helper function for split_array.

    Arguments:
        arr {List[int]} -- list of numbers to divide into 2 sublists of equal value.
        index {int} -- the index of the current value in the list.

    Returns:
        True if lst can be divided into 2 sublists of equal value,
    """
    # base case
    if index == count(arr) or not arr:
        return False
    # check whether the sum of the first part of the list is equal to the sum of the latter part of the list
    if sum_list(arr[:index]) == sum_list(arr[index:]):
        return True
    # Recursive case
    # it will recursive with the index plus 1
    return split_array2(arr, index + 1)


def split_array(lst: List[int]) -> bool:
    """Determine if it possible to divide a list (lst) at some index
    such that the sum of values in the first part of the list equals 
    the sum in the latter part of the list.  No loops are used.

    This function should not modify the parameter.

    :param lst:  list of numbers to divide into 2 sublists of equal value.
    :returns:    True if lst can be divided into 2 sublists of equal value, 
                 False otherwise.

    Examples:
    >>> split_array([2, 2])
    True
    >>> split_array([2, 3])
    False
    >>> split_array([1, 2, 3, 4])
    False
    >>> split_array([1, 2, 3, 4, 10])
    True

    You should define a helper function. This function calls the helper,
    and the helper function performs the recursion.
    """
    return split_array2(lst)
