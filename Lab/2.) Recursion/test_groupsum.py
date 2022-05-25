"""Pytest test for groupsum.
Requires plugins:  pytest pytest-timeout
"""
import pytest
TIME_LIMIT=2     # test runtime limit in seconds


"""test groupsum"""
from groupsum import groupsum
@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "total, array, expected",
    [
        (0, [1,2,3], []),          # edge case
        (5, [5], [5]),             # edge case
        (6, [5], []),              # impossible edge case
        (6, [1,5], [1,5]),
        (15, [5,4,3,2,1], [5,4,3,2,1]),
        (15, [30,40,5,4,3,2,1], [5,4,3,2,1]),
        (15, [40,20,5,4,3,2,1], [5,4,3,2,1]),
        (17, [10,8,2,4,2,14,3,8], [8,2,4,3]),   # don't be greedy
        (16, [5,4,3,2,1], None),
        (15, [8,4,4,2,2,2,2], None),
        (1,  [2,2,2], None),
        (2,  [1], None),
    ])
def test_groupsum(total, array, expected):
    result = groupsum(total, array)
    if expected is None:
        assert result is None
    else:
        # don't require any specific order of elements in array
        assert sort(expected) == sort(result)

def sort(lst):
    if isinstance(lst, list):
        return lst.sort()
    else:
        return lst