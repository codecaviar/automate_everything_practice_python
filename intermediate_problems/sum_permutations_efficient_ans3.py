# Automate Everything from @codecaviar
# Level: Intermediate
# Updated: 2020-11-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

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

    from math import factorial as fact

    s = str(num)
    perms = fact(len(s) - 1)
    coefAll = int('1' * len(s))

    return coefAll * perms * sum(map(int,s))

    # The following solution also works using itertools.permutations
    # return sum(int("".join(x)) for x in permutations(str(num)))
