# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def find_digits(n, p):
    """
    Given a positive integer n written as abcd... (a, b, c, d... being
    digits) and a positive integer p: we want to find a positive
    integer k, if it exists, such as the sum of the digits of n taken
    to the successive powers of p is equal to k * n.

    Is there an integer k such as :
    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

    Parameters
    ----------
    n: {int} written as abcd... (a, b, c, d... being digits)
    p: {int} positive integer

    Returns
    -------
    {int}: k, if exists, sum of the digits of n taken to the successive
    powers of p is equal to k * n; otherwise, return -1

    Example
    -------
    >>> find_digits(3456789, 5)
    -1
    >>> find_digits(249, 1)
    3
    >>> find_digits(7388, 2)
    5
    """

    s = 0
    for i, c in enumerate(str(n)): # turn integer into digits
        s += pow(int(c),p+i) # apply number properties
    return int(s/n) if s % n == 0 else -1 # return result if k exists 
