# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import math # need to use library

def round_century(year):
    """
    First century spans from the year 1 up to and including year 100,
    while second year from year 101 up to and including year 200, etc.

    Parameters
    ----------
    year: {int} givne a year as integer

    Returns
    -------
    {int}: return only the century

    Example
    -------
    >>> round_century(815963)
    8160
    >>> round_century(7025)
    71
    >>> round_century(360593)
    3606
    >>> round_century(91)
    1
    >>> round_century(2000)
    20
    """

    # Optional: use try...except block to handle error conditions

    return int(math.ceil(year / 100.0)) * 1 # math.ceil will round down
    # use division by 100.0 to focus on the year
