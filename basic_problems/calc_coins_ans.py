# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def calc_coins(cents):
    """
    Given a cents value, return minimum number of coins of same value.
    The function should return an array where
        coins[0] = pennies ==> $00.01
        coins[1] = nickles ==> $00.05
        coins[2] = dimes ==> $00.10
        coins[3] = quarters ==> $00.25

    Parameters
    ----------
    cents: {int} values of cents

    Returns
    -------
    {list}: coins array with the minimum number of coins of equal value

    Example
    -------
    >>> calc_coins(53)
    [3, 0, 0, 2]
    >>> calc_coins(37)
    [2, 0, 1, 1]
    >>> calc_coins(42)
    [2, 1, 1, 1]
    """

    # Optional: use try...except block to handle error conditions

    results = [0] * 4 # create empty array of zeros
    coins = [1, 5, 10, 25] # define coin values
    c = cents

    for i in [3, 2, 1, 0]:
        results[i] = c // coins[i] # use floor division
        c = c - (results[i] * coins[i]) # update current value of cents
    return results
