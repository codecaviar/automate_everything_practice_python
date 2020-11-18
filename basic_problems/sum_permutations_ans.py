# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import math # use math.factorial to calculate n!

def sum_permutations(num):
    """
    Find the sum of all numbers with the same digits(permutations) including duplicates - use efficient algorithms

    Parameters
    ----------
    num: {int} integer with various number of digits

    Returns
    -------
    {int}: sum of all digits and pemutations

    Example
    -------
    >>> sum_permutations(9665158017)
    19353599998064640
    >>> sum_permutations(1579294917)
    21772799997822720
    >>> sum_permutations(632493041)
    143359999856640
    """

    # Optional: use try...except block to handle error conditions

    n = len(str(num))
    digitsum = sum([int(x) for x in list(str(num))])
    return (sum((10 ** i) * digitsum
        * math.factorial(n - 1) for i in range(0, n)))

    # The following solution also works using itertools.permutations
    # return sum(int("".join(x)) for x in permutations(str(num)))
