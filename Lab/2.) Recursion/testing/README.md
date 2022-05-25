## Test the Recursion Lab using Pytest

Pytest is a Python plugin, not part of the standard Python distribution.
Install it using pip3.  My tests also use the pytest-timeout plugin to prevent testsfrom running forever.

To install both packages:
```
pip3 install --upgrade pytest pytest-timeout
```
I prefix this command with "sudo " to install plugins globally (not in my home dir).


### Run doctests using Pytest

Run the doctests (from the starter code) and print nicely formatted results:
```
pytest --doctest-modules
```

Run doctests for just one module, say, groupsum:
```
pytest --doctect-modules groupsum.py
```
but in that case, its more informative to run doctest directly:
```
python3 -m doctest -v groupsum.py
```

### Run My pytests

A student might modify or delete the doctest comments in some files,
so I don't think doctest is a thorough test of their code.
This repo contains parameterized pytests for each problem in the lab:

| File               | Tests for |
|--------------------|-----------|
| `test_all.py`      | All problems **except** groupsum |
| `test_groupsum.py` | groupsum |


Run all tests with nicely formatted output:
```
pytest -v
```

Run tests for only the `split_array` problem:
```
pytest -v -k split_array
```

Run only the `test_groupsum.py` file:
```
pytest -v test_groupsum.py
```
or
```
pytest -v -k groupsum
```

### Code Inspection

Students should **not** use "for", "while", list comprehensions, or `sum()` in their code. `sum()` is OK (groupsum and `split_array`) if they also use recursion.


### Note to TAs

Feel free to combine `test_groupsum` into `test_all` if its convenient.

I separated them in case students make syntax errors in groupsum,
which makes the output harder to read.

Also, if add any more test cases please commit them back to the repo!
