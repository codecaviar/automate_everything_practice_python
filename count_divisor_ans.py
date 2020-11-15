# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-14

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def count_divisor(n):
    """
    Count the number of divisors of a positive integer n

    Parameters
    ----------
    n: {int} postive integer

    Returns
    -------
    {int}: count

    Example
    -------
    >>> count_divisor(30)
    8
    >>> count_divisor(12)
    6
    >>> count_divisor(4)
    3
    """

    # Optional: use try...except block to handle error conditions

    count = 0
    for n_div in range(1, n+1):

        if n % n_div == 0:
            count += 1
        else:
            continue

    return count
