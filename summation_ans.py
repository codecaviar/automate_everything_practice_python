# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def summation(num):
    """
    Find the summation of every number from 1 to num.
    The number will always be a positive integer greater than 0.

    Parameters
    ----------
    num: {int} postive integer greather than 0

    Returns
    -------
    {int}: sum of all numers from 1 to num

    Example
    -------
    >>> summation(8)
    36
    >>> summation(22)
    253
    >>> summation(213)
    22791
    """

    # Optional: use try...except block to handle error conditions

    # The range() function returns a range object (a type of iterable).
    new_sum = sum(range(num + 1))

    return new_sum
