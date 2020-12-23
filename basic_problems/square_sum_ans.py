# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def square_sum(num):
    """
    Given an array, square each number and return the sum

    Parameters
    ----------
    num: {list} array of integers

    Returns
    -------
    {int}: sum of all squared numbers in the list

    Example
    -------
    >>> square_sum([7, 11, 10, -7, -20, -9, 4, -1])
    817
    >>> square_sum([10, 4, 15, 15, 12, -16, 7, 19, -15, -20])
    2001
    >>> square_sum([-11, 16, -17, -10, 13, -6, -6, -3])
    1016
    """

    # Use generator and list comprehension
    return sum([x ** 2 for x in num])
