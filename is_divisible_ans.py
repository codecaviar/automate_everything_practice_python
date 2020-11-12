# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-07

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def is_divisible(n, x, y):
    """
    Check if a number is divisible by two other numbers

    Parameters
    ----------
    n: {int} positive, non-zero integer
    x: {int} positive, non-zero integer
    y: {int} positive, non-zero integer

    Returns
    -------
    {bool}: True if n is divisible by x AND y, else False

    Example
    -------
    >>> is_divisible(100, 5, 3)
    False
    >>> is_divisible(340, 4, 17)
    True
    >>> is_divisible(780, 4, 13)
    True
    """

    # Optional: use try...except block to handle error conditions
    # Function will return Boolean value based on condition statement
    return n % x == 0 and n % y == 0
