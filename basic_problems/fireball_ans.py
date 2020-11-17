# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def fireball(power_level, num_dragons):
    """
    If it takes three fireballs to defeat one dragon, return whether 
    or not the wizard has enough fireballs to escape the dungeon.

    Parameters
    ----------
    power_level: {int} postive number of fireballs remaining
    num_dragons: {int} positive number of dragons remaining

    Returns
    -------
    {bool}: true or false whether the wizard will escape the dungeon

    Example
    -------
    >>> fireball(3, 1)
    True
    >>> fireball(0, 1)
    False
    >>> fireball(10, 10)
    False
    """

    # Optional: use try...except block to handle error conditions

    # Boolean expression is an expression that evaluates to produce
    # a result which is a Boolean value, so there is no need to specify # separate True and False values to return
    return power_level >= num_dragons * 3
