"""Tests of recursion problems in Lab 2, except groupsum.

Requires: pytest and pytest-timeout (for timeout annotation)

Install packages:
    pip3 install --upgrade pytest pytest-timeout

or (I install packages globally)
    sudo pip3 install --upgrade pytest pytest-timeout

Run all tests:
    pytest -v     (auto-discovers test_*.py)

Run only tests for split_array
    pytest -v -k split_array

Run doctest tests in all *.py files
    pytest --doctest-modules

"""
from unique import unique
from tribonacci import tribonacci
from split_array import split_array
from longest_word import longest_word
from flatten import flatten
from power import power
from fibonacci import fibonacci
import pytest
TIME_LIMIT = 2     # test runtime limit in seconds


"""test fibonacci"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "n, result",
    [
        (1, 1),
        (0, 0),
        (5, 5),
        (20, 6765),
        (44, 701408733),   # this will timeout if solution is incorrect
    ])
def test_fibonacci(n, result):
    assert fibonacci(n) == result


"""test power"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "base, exponent, result",
    [
        (16, 0, 1),
        (16, 1, 16),
        (2, 20, 1024*1024),
        (2, 40, 1024*1024*1024*1024),
        (10.0, 6, 1000000.0),
        (0, 3, 0),
    ])
def test_power(base, exponent, result):
    assert power(base, exponent) == result


"""test flatten"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "lst, result",
    [
        ([], []),                 # edge case
        ([1], [1]),               # another edge case
        (['a', 'b'], ['a', 'b']),   # flat already
        ([['a', 'b'], 'c'], ['a', 'b', 'c']),
        (['a', ['b', ['c']]], ['a', 'b', 'c']),
        ([1, [10, 20], 2, [3, [[4, 5], 6], [], 7], 8],
         [1, 10, 20, 2, 3, 4, 5, 6, 7, 8]),
    ])
def test_flatten(lst, result):
    assert flatten(lst) == result


"""test longest_word"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "string, result",
    [
        ("", ""),
        (" \t\t   ", ""),
        (" #1 ", "#1"),
        ("The longest word is?", "longest"),
        ("Long longer and longest!!!", "longest!!!"),
        ("Long  a n d    longest !!!", "longest"),
    ])
def test_longest_word(string, result):
    assert longest_word(string) == result


"""test split_array"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "array, result",
    [
        ([2, 2, 2, 2], True),
        ([2, 2, 2, 3], False),
        ([1, 2, 3, 0, 0, 1, 5], True),
        ([1, 2, 3, 0, 0, 1, 6], False),
        ([1, 2, 3, 0, 0, 1, 7, 0, 0], True),
    ])
def test_split_array(array, result):
    assert split_array(array) == result


"""test tribonacci"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "n, result",
    [
        (1, 1),
        (0, 0),
        (5, 7),
        (10, 149),
        (20, 66012),
    ])
def test_tribonacci(n, result):
    assert tribonacci(n) == result


"""test unique"""


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "testlist, result",
    [
        ([4], [4]),                    # edge case
        (['a', 'b', 'c'], ['a', 'b', 'c']),
        (['a', 'a', 'a'], ['a']),
        ([5, 4, 5, 5, 2, 4], [5, 4, 2]),
        (['a', 'aaa', 'a', 'aa', 'aa'], ['a', 'aaa', 'aa']),
    ])
def test_unique(testlist, result):
    assert unique(testlist) == result
