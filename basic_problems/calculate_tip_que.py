# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

from math import ceil # use ceil to calculate tip

def calculate_tip(amount, rating):
    """
    Calculate how much you need to tip based on the total amount of the
    bill and the service. You need to consider the following ratings:

    Terrible: tip 0%
    Poor: tip 5%
    Good: tip 10%
    Great: tip 15%
    Excellent: tip 20%

    Parameters
    ----------
    amount: {float} bill amount
    rating: {str} case insensitive

    Returns
    -------
    {int}: round tip up

    Example
    -------
    >>> calculate_tip(82, "GooD")
    9
    >>> calculate_tip(6, "terrIblE")
    0
    >>> calculate_tip(9, "EXceLl,NT")
    'Rating not recognised'
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
