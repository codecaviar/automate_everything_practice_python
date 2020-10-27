# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-26

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def make_pyramid(n):
    """
    Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

    Parameters
    ----------
    n: {int} number greater than or equal to zero

    Returns
    -------
    {list}: list of lists containing only one values

    Example
    -------
    >>> make_pyramid(0)
    [ ]
    >>> make_pyramid(1)
    [ [1] ]
    >>> make_pyramid(2)
    [ [1], [1, 1] ]
    >>> make_pyramid(3)
    [ [1], [1, 1], [1, 1, 1] ]
    """

    # Optional: use try...except block to handle error conditions

    new_pyramid = []

    for i in range(1, n + 1):
        new_pyramid.append([1] * i) # multiple arrays with the one value

    return new_pyramid
