import re
def grep(string, filename):
    """print each line from a file that contain string
    :param string: is string to search for
    :param filename: name of a file
    """
    lines = [line for line in open(filename).read().splitlines() if line]
    for line in lines:
        if re.search(string, line):
            print(line)
