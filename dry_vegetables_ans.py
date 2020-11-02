# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-30

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def dry_vegetables(p0, w0, p1):
    """
    Calculate the final weight of vegetables after cooking

    Parameters
    ----------
    p0: {int} initial percent of water in vegetables
    w0: {int} initial weight of vegetables
    p1: {int} final percent of water in vegetables

    Returns
    -------
    {int}: final weight of vegetables (w1) truncated as an int

    Example
    -------
    >>> dry_vegetables(92, 155, 89)
    112
    >>> dry_vegetables(84, 92, 81)
    77
    >>> dry_vegetables(75, 248, 71)
    213
    """

    # Optional: use try...except block to handle error conditions

    water0 = w0 * p0 / 100.0 # calculate initial weight of water
    dry0 = w0 - water0 # calculate initial dry weight of vegetables
    w1 = round(dry0 * 100 / (100.0 - p1), 2) # calculate final weight

    return int(w1) # truncate to an integer
