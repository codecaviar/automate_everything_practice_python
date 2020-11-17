# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-11

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def is_divisible2(num):
    """
    Given an integer num (1 <= num <= 100), check whether you can
    divide the integer evenly

    Parameters
    ----------
    num: {int} greather than 0, but less than or equal to 100

    Returns
    -------
    {bool}: True if it is divisible by 2, else False

    Example
    -------
    >>> is_divisible2(100)
    True
    >>> is_divisible2(5)
    False
    >>> is_divisible2(63)
    False
    """

    # Optional: use try...except block to handle error conditions

    return num % 2 == 0 # use modulo operator to check remainder
