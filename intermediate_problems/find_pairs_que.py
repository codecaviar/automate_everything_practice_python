# Automate Everything from @codecaviar
# Level: Intermediate 
# Updated: 2020-11-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

def total_sum(x):
    """
    The divisors of a positive integer n are said to be proper when you
    consider only the divisors other than n itself. In the following
    description, divisors will mean proper divisors. For example for
    100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

    Parameters
    ----------
    x: {int} normal number to find divisor

    Returns
    -------
    {int}: sum of all proper divisors, not including the original

    Example
    -------
    >>> total_sum(50)
    43
    >>> total_sum(10)
    8
    >>> total_sum(100)
    117
    >>> total_sum(48)
    76
    >>> total_sum(75)
    49
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required


def find_pairs(start, stop):
    """
    Let s(n) be the sum of these proper divisors of n. Call buddy two
    positive integers such that the sum of the proper divisors of each
    number is one more than the other number:

    (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

    Parameters
    ----------
    start: {int} lower range of numbers
    stop: {int} upper range of numbers

    Returns
    -------
    {list}: first pair (n, m), such that n is between start and stop,
    inclusive, where possible for m > stop, requirement for m > n

    Example
    -------
    >>> find_pairs(310, 2755)
    [1050, 1925]
    >>> find_pairs(2382, 3679)
    'Nothing'
    >>> find_pairs(1950, 6426)
    [2024, 2295]
    >>> find_pairs(2177, 4357)
    'Nothing'
    >>> find_pairs(9207, 10482)
    [9504, 20735]
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
