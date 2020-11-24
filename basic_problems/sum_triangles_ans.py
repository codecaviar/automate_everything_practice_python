# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-19

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def sum_triangles(n):
    """
    Triangular Number: "any of the series of numbers (1, 3, 6, 10, etc)
    obtained by continued summation of the natural numbers 1, 2, 3, etc"

    [01]
    02 [03]
    04 05 [06]
    07 08 09 [10]
    11 12 13 14 [15]
    16 17 18 19 20 [21]

    Parameters
    ----------
    n: {int} natural number to calculate triangular number

    Returns
    -------
    {int}: ...

    Example
    -------
    >>> sum_triangles(94)
    145163820
    >>> sum_triangles(-5)
    0
    >>> sum_triangles(177)
    939929
    """

    # Optional: use try...except block to handle error conditions

    if n <= 0: # edge case for zero
        result = 0
    else: # use list comprehension for n * (n+1) / 2
        result = sum([x * (x + 1) // 2 for x in range(1,n+1)])

    return result
