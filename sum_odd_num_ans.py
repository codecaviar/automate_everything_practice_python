# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-26

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def sum_odd_num(n):
    """
    Given a triangle of consecutive odd numbers

                 1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29
    ...

    Calculate the row sums of this triangle from the row index
    (starting at index 1)

    Parameters
    ----------
    n: {int} row index of triangle of consecutive odd numbers

    Returns
    -------
    {int}: sum of all consecutive odd numbers in row of triangle

    Example
    -------
    >>> sum_odd_num(1)
    1
    >>> sum_odd_num(2)
    8
    >>> sum_odd_num(3)
    27
    >>> sum_odd_num(313)
    30664297
    >>> sum_odd_num(132)
    2299968
    """

    # Optional: use try...except block to handle error conditions

    return n ** 3
