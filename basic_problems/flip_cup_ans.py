# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def flip_cup(num):
    """
    With n cups as a1, a2, ..., an. Each of those cups can be
    either 0 or 1 (flipped or not flipped). Player allowed to do
    exactly one move: choose two indices i and j (1 ≤ i ≤ j ≤ n) and
    flips all values ak for which their positions are in range [i, j]
    (that is i ≤ k ≤ j). Flip the value of x means to apply operation
    x = 1 - x. The goal of the game is that after exactly one move to
    obtain the maximum number of ones

    Parameters
    ----------
    num: {list} n integers: a1, a2, ..., an. 1 ≤ n ≤ 100.
    It is guaranteed that each of those n values is either 0 or 1

    Returns
    -------
    {int}: the maximal number of 1s that can be obtained after exactly
    one move

    Example
    -------
    >>> flip_cup([1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1])
    11
    >>> flip_cup([0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1])
    58
    >>> flip_cup([1, 0, 1, 0, 0])
    4
    """

    current = 0
    biggest = 0

    for i in num:
        current = max(0, current - ( i or -1 )) # compare current num
        biggest = max(biggest, current) # find new max

    return sum(num) + (biggest or -1) # return max num of 1s
