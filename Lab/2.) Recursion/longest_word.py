def count(word: str) -> int:  # sourcery skip: assign-if-exp
    """count len of word by using recursion

    Arguments:
        word {str} -- some word

    Returns:
        int -- len of word
    """

    if not word:  # Basecase
        return 0
    else:
        # Recursive case
        # it will count the len of the word and then it will call the function again
        return 1 + count(word[:-1])


def longest_word(phrase: str) -> str:
    """Return the longest 'word' in a phrase.

    A 'word' is any sequence of characters not including whitespace.
    Solve this by recursion (of course).
    Hint: "i hate strings".split(maxsplit=1)  what does this return?

    Arguments:
        phrase {str} -- some phrase
    
    Returns:
        str -- longest word in phrase

    By using recursion

    Examples:
    >>> longest_word("Which is the longest?")
    'longest?'
    >>> longest_word("There are 60 students in Programming 2")
    'Programming'
    >>> longest_word('Learn recursion at https://realpython.com/python-recursion')
    'https://realpython.com/python-recursion'
    >>> longest_word('singleton')
    'singleton'
    >>> longest_word('')
    ''
    """
    # Basecase
    # if the phrase is empty, return an empty string
    if not phrase.strip():
        return ''
    word = phrase.split(maxsplit=1)[0]  # get the first word
    # Recursive case
    # it will split the phrase into two parts
    # then it will call the function again
    # if the word is longer than the longest word, it will return the word
    if count(word) > count(longest_word(phrase[count(word):].strip())):
        return word
    # return the longest word
    return longest_word(phrase[count(word):])

    # ma friend solution
    # if not phrase.strip():
    #     return ''
    # text = phrase.split(maxsplit=1)
    # first = text[0]
    # try:
    #     if len(longest_word(text[1])) > len(first):
    #         return longest_word(text[1])
    #     else:
    #         return longest_word(first)
    # except IndexError:
    #     return phrase.strip()
