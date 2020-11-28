# Automate Everything from @codecaviar
# Level: Intermediate
# Updated: 2020-11-21

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def find_longest_substr(input_str):
    """
    Given a string, find the length of the longest substring
    without repeating characters

    Parameters
    ----------
    input_str: {str} a string with possible substring(s)

    Returns
    -------
    {int}: length of longest substring

    Example
    -------
    >>> find_longest_substr('abcabcbb')
    3
    >>> find_longest_substr('bbbbb')
    1
    >>> find_longest_substr('pwwkew')
    3
    >>> find_longest_substr('')
    0
    """

    # Optional: use try...except block to handle error conditions

    n = len(input_str)
    result = 0
    mp = {} # stores the current index of a character
    i = 0
    # try to extend the range [i, j]
    for j in range(n): # go through entire length of string
        if input_str[j] in mp: # check if char already in map
            i = max(mp[input_str[j]], i) # find larger index
        else:
            pass
        # current index j - lenth of result i, add one for string
        result = max(result, j - i + 1) # update result
        mp[input_str[j]] = j + 1 # update index of char in map

    return result
