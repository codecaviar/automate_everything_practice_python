# Automate Everything from @codecaviar
# Level: Intermediate
# Updated: 2020-11-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def total_sum(x):
    """
    The divisors of a positive integer n are said to be proper when you
    consider only the divisors other than n itself. In the following
    description, divisors will mean proper divisors. For example for
    100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

    Parameters
    ----------
    x: {int} normal number to find divisor

    Returns
    -------
    {int}: sum of all proper divisors, not including the original

    Example
    -------
    >>> total_sum(50)
    43
    >>> total_sum(10)
    8
    >>> total_sum(100)
    117
    >>> total_sum(48)
    76
    >>> total_sum(75)
    49
    """
    result = []
    for i in range(1, int(x**0.5) + 1): # upper range is divided by 2
        if not x % i: # check if number is has no remainder
            result.append([i, x//i])
        else:
            pass
    # find the set of all divisors, and then add together
    return sum(set(num for pair in result for num in pair)) - x


def find_pairs(start, stop):
    """
    Let s(n) be the sum of these proper divisors of n. Call buddy two
    positive integers such that the sum of the proper divisors of each
    number is one more than the other number:

    (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

    Parameters
    ----------
    start: {int} lower range of numbers
    stop: {int} upper range of numbers

    Returns
    -------
    {list}: first pair (n, m), such that n is between start and stop,
    inclusive, where possible for m > stop, requirement for m > n

    Example
    -------
    >>> find_pairs(310, 2755)
    [1050, 1925]
    >>> find_pairs(2382, 3679)
    'Nothing'
    >>> find_pairs(1950, 6426)
    [2024, 2295]
    >>> find_pairs(2177, 4357)
    'Nothing'
    >>> find_pairs(9207, 10482)
    [9504, 20735]
    """

    for n in range(start, stop):
        s_m = n + 1
        s_n = total_sum(n) # find sum of divisors
        m_candidate = s_n - 1 # calculate initial candidate for m

        if (m_candidate < start): # apply return constraint
            continue
        elif (total_sum(m_candidate) == s_m): # check sum of divisors
            return [n, m_candidate] # return appropriate n,m inclusive
        else:
            continue

    return 'Nothing'
