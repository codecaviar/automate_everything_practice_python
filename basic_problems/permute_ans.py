# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-22

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def permute(num, input_str):
    """
    Find all possible order of arrangements of a given set of letters
    Apply backtracking (form of recursion) to verify is pair already
    treated or not by the algorithm

    Parameters
    ----------
    num: {int} desired number of letters in permutation
    input_str: {list} available letters to check

    Returns
    -------
    {list}: all possible permutations of a given set of letters

    Example
    -------
    >>> permute(1, ["a", "b", "c"])
    ['a', 'b', 'c']
    >>> permute(2, ["a", "b", "c"])
    ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    >>> permute(3, ["a", "b", "c"])
    ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']
    """

    if num == 1: # edge case for a single character
        return input_str
    else: # use backtracking to find arrangements
        return [ y + x
                 for y in permute(1, input_str) # use recursive 
                 for x in permute(num - 1, input_str)
                 ]
