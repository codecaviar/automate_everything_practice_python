# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-1224

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def convert_number(n):
    """
    Given a random non-negative number, you have to return
    the digits of number within an array in reverse order

    Parameters
    ----------
    n: {int} intger

    Returns
    -------
    {list}: array of integers

    Example
    -------
    >>> convert_number(14305)
    [5, 0, 3, 4, 1]
    >>> convert_number(173675515)
    [5, 1, 5, 5, 7, 6, 3, 7, 1]
    >>> convert_number(34941613588)
    [8, 8, 5, 3, 1, 6, 1, 4, 9, 4, 3]
    """

    # Use map to convert a reverse string as integer
    # Convert number into a list
    return list(map(int, str(n)[::-1]))
