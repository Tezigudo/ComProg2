"""The docstring comments in this file use the Restructured Text markup style.
It is one of 3 commonly used formats. This format is recognized by the Sphinx
documentation generator.
To learn more see https://gist.github.com/nipunsadvilkar/fec9d2a40f9c83ea7fd97be59261c400
"""
from typing import List


def flatten(lst: List[str]) -> List[str]:
    """Flatten a list containing other lists, so the result
    is a list of elements that are not lists.

    The return value contains all elements in the same order as the original list,
    but linearized.  The parameter lst is not modified.

    :param lst: a list that possibly contains other lists as elements.
    :returns: a new list containing a linearized version of the parameter.

    Examples:
    >>> flatten([])
    []
    >>> flatten(['a', 'b'])  # flat already
    ['a', 'b']
    >>> flatten([['a', 'b'], 'c'])
    ['a', 'b', 'c']
    >>> flatten(['a', ['b', 'c']])
    ['a', 'b', 'c']
    >>> flatten(['b', ['c', ['d', 'e']]])
    ['b', 'c', 'd', 'e']
    >>> flatten([[[['a',['b'],'c']]], 'bye'])
    ['a', 'b', 'c', 'bye']
    >>> flatten(['a', [10,20], 2, [3,[[4,5],'cat'], [], 4], 50])
    ['a', 10, 20, 2, 3, 4, 5, 'cat', 4, 50]
    """
    # Basecase
    # if the list is empty, return an empty list
    if not lst:
        return []
    # if the list is not empty, check if the first element is a list
    # if it is a list, call the function again with the first element
    if isinstance(tmp := lst[0], list):
        return flatten(tmp) + flatten(lst[1:])
    # if the first element is not a list, return the first element
    # and call the function again with the rest of the elements
    return [tmp] + flatten(lst[1:])


if __name__ == '__main__':
    flatten([1, [2, [3, 4], 5]])
