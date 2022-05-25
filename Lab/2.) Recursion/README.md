## Recursion Problems

Each Python file contains a single function to implement using recursion.

1. Implement the function according to the docstring comments in each file.
2. Do not use a loop or shortcut the solution by using a Python built-in function or list comprehension.  Use recursion.
3. Each file contains doctests in the comments.  To run the doctests use:
   ```
   python3 -m doctest filename.py
   # for a list of tests done, including passing tests:
   python3 -m doctest -v filename.py
   ```


Easy problems:

* power.py - compute powers of a number
* tribonacci.py - compute values of a Fibonacci-like series
* longest\_word.py - return the longest word in a string
* unique.py - return unique elements in a list
* flatten.py - "flatten" a list containing nested lists

Problems using a Helper Function:

* fibonacci.py - fast recursive computation of Fibonacci numbers
* split_array.py - divide a list into 2 equal valued sublists

Problem using Backtracking:

* groupsum.py

## What to Submit

Push your work to Github when done.

## How to Solve

1. Identify the Base Case where recursion stops.  There may be more than one "base" condition.
2. Identify the recursion step. The recursive call should make the problem smaller.
3. If you are stuck, try solving small problems yourself on paper, using recursion. Observe how you solve it.
