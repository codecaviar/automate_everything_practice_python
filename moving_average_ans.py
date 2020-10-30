# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-26

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def moving_average(values, n):
    """
    Calculate the moving average based on a defined window

    Parameters
    ----------
    values: {list} list of integers
    n: {int} size of the window

    Returns
    -------
    {list}: list of floats, if n is equal to zero or greater than the length of the list of input values, return None

    Example
    -------
    >>> moving_average([316, 445, 98, 185, 333, 410, 478], 6)
    [297.8333333333333, 324.8333333333333]
    >>> moving_average([40, 30, 50, 46, 39, 44], 7)

    >>> moving_average([278, 1, 379, 213, 286, 472, 75], 3)
    [219.33333333333334, 197.66666666666666, 292.6666666666667, 323.6666666666667, 277.6666666666667]
    """

    # Optional: use try...except block to handle error conditions

    if n == 0 or n > len(values): # check for edge case to return None
        new_calc = None
    else:
        new_calc = []
        # Use a range function to define number of window calculations
        for i in range(0, len(values) - n + 1):
            # Calculate moving average based on each window
            new_calc.append(sum(values[i:i+n]) / n)

    return new_calc
