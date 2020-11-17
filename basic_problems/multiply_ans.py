# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def multiply(n1, n2):
    """
    Return the product of two numeric values

    Parameters
    ----------
    n1: {int, float, complex} first numberic value to multiply
    n2: {int, float, complex} second numeric value to multiply

    Returns
    -------
    {int, float, complex}: product of two numeric values
        or return 'TypeError' message otherwise

    Example
    -------
    >>> multiply(1, 1)
    1
    >>> multiply(2.5, 2)
    5.0
    >>> multiply("3", 5)
    'TypeError: unsupported operand type(s) for *'
    """

    # Optional: use try...except block to handle error conditions

    if isinstance(n1, (int, float, complex)) \
        and isinstance(n2, (int, float, complex)):
        new_product = n1 * n2

    else:
        new_product = 'TypeError: unsupported operand type(s) for *'

    return new_product
