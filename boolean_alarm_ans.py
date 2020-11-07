# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-06

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def boolean_alarm(home, away):
    """
    Return True if you are at home or away from your house

    Parameters
    ----------
    home: {bool} true whenever you are home sleeping
    away: {bool} true whenever you are away working

    Returns
    -------
    {bool}: Return False for all circumstances you do not set an alarm

    Example
    -------
    >>> boolean_alarm(True, False)
    True
    >>> boolean_alarm(False, False)
    False
    >>> boolean_alarm(True, True)
    True
    """

    # Optional: use try...except block to handle error conditions

    return home == True or away == True
