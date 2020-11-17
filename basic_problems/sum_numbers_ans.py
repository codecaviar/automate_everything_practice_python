# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def sum_numbers(num1, num2):
    """
    Given two integers num1 and num2, which can be positive or
    negative, find the sum of all the numbers between including them
    too and return it. If the two numbers are equal return num1 or num2.

    Parameters
    ----------
    num1: {integer} first number
    num2: {integer} second number, not ordered

    Returns
    -------
    {int}: sum of all numbers between and including num1 and num2

    Example
    -------
    >>> sum_numbers(5, 1)
    15
    >>> sum_numbers(17, 17)
    17
    >>> sum_numbers(-505, 4)
    -127755
    """

    # Optional: use try...except block to handle error conditions

    if num1 == num2:
        return num1 # check if two integers are the same
    else: # create a list, based on min and max of the two inters
        return sum(list(range(min(num1, num2), max(num1, num2) + 1)))
