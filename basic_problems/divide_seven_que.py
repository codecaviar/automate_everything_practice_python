# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

def divide_seven(m, step=0):
    """
    A number m of the form 10x + y is divisible by 7 if and only if
    x − 2y is divisible by 7. In other words, subtract twice the last
    digit from the number formed by the remaining digits. Continue to
    do this until a number known to be divisible or not by 7 is
    obtained; you can stop when this number has at most 2 digits
    because you are supposed to know if a number of at most 2 digits is
    divisible by 7 or not.

    Parameters
    ----------
    m: {int} original number
    step: use recursive function to repeat steps

    Returns
    -------
    {tup}: return a 2 digit number, and number of steps

    Example
    -------
    >>> divide_seven(477557101)
    (28, 7)
    >>> divide_seven(477557102)
    (47, 7)
    >>> divide_seven(2340029794923400297949)
    (14, 20)
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
