# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def enough_space(cap, on, wait):
    """
    Check if there is enough space on the truck for more boxes,
    return 0 if there is space, the number of unshipped boxes

    Parameters
    ----------
    cap: {int} capacity of the truck
    on: {int} current number of boxes on the truck
    wait: {int} number of new boxes to be added to the truck

    Returns
    -------
    {int}: 0 if all waiting boxes fit, else number of unshipped boxes

    Example
    -------
    >>> enough_space(61, 46, 18)
    3
    >>> enough_space(53, 53, 44)
    44
    >>> enough_space(20, 5, 6)
    0
    """

    # Optional: use try...except block to handle error conditions

    # Use conditional statement to check if there is enough space
    # Use absolute value to get difference in boxes when over capacity
    return 0 if cap >= on + wait else abs(cap - on - wait)
