from typing import List

def unique(values: List[str]) -> List:
    """Given a list of values return a sublist containing only one
    unique occurence of each value in the parameter list, in the order 
    that the values first appeared in the parameter list.

    :param values: a list of values to search for unique elements
    :returns: a new list containing the first unique occurence of values 
    in the parameter list. If the parameter is an empty list, return an 
    empty list.

    Examples:
    >>> unique(['a','b','c'])
    ['a', 'b', 'c']
    >>> unique(['a','c','b','b','c','a','b'])
    ['a', 'c', 'b']
    >>> unique(['a', 'a', 'a', 'b', 'a', 'b', 'b'])
    ['a', 'b']
    >>> unique([])
    []
    >>> unique([1, 2, 4, 2, 1, 4, 0])
    [1, 2, 4, 0]
    """

    # if the list is empty, return an empty list
    if not values:
        return []
    # Recursive case
    lst = unique(values[:-1])  # call the function again with the rest of the elements

    # if the first element is not in the list, return the first element
    # and call the function again with the rest of the elements
    if (element := values[-1]) not in lst:
        lst.append(element)
    # Basecas
    return lst
