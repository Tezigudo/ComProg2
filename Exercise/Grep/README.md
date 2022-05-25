## Search for Strings

Create a file named `grep.py` containing this function:
```python
grep(string, filename)
    """Print each line from a file that contains the string anywhere on the line.
    
    :param string:  is the string to search for
    :param filename: name of a file
    """
```

### Test It

Ffor one of your Python files containing code, do:
```
>>> grep("def", "somefile.py")
```

### Hints:
1. To open a file use:   `file = open("filename", "r")` or `open("filename")`
2. To check if a line contains a string, use:
   ```python
   import re
   if re.search(string, line):
       # the line contains the string
   else:
       # the line does not contain the string
    ```
    
