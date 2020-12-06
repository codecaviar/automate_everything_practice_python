# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import math # use ceil and log

def grains_chess(num):
    """
    Person asks, as compensation, only 1 grain of rice for the first
    square, 2 grains for the second, 4 for the third, 8 for the fourth
    and so on, always doubling the previous. Given an amount of grain,
    calculate to which square one needs to land on to reach at least
    that amount of grain.

    Parameters
    ----------
    num: {int} amount of grain, valid, reasonable, non negative

    Returns
    -------
    {int}: chessboard square

    Example
    -------
    >>> grains_chess(94354)
    17
    >>> grains_chess(249)
    8
    >>> grains_chess(369)
    9
    """

    # Total grains at square n is x = (2 ** n) - 1
    # Thus, n = log2(x + 1)
    # Use only floats, then convert back to integer
    return int(math.ceil(math.log(float(num + 1), 2)))
