# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2021-06-01

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def power_ofi(n):
    """
    i is the imaginary unit defined as i^2 = -1

    Parameters
    ----------
    n: {int} non-negative integer

    Returns
    -------
    {str}: string of the power of i and may contain i

    Example
    -------
    >>> power_ofi(0)
    '1'
    >>> power_ofi(281)
    'i'
    >>> power_ofi(353)
    '-1'
    >>> power_ofi(151)
    '-i'
    """

    # When raising i to any positive integer power, the answer is always
    # on of the following: i, -1, -1, or 1
    return {0:"1", 1:"i", 2:"-1", 3:"-i"}[n % 4]
