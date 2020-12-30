# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

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

    tips = {
        'terrible': 0,
        'poor' : .05,
        'good' : .1,
        'great' : .15,
        'excellent' : .2
    }

    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'
