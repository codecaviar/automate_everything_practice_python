# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def multiple_table(num):
    """
    Return multiplication table from 1 to 10 for any input integer,
    use "\n" in string to jump to the next line

    Parameters
    ----------
    num: {int} any number, including 0 and negtative

    Returns
    -------
    {str}: print string of multiplcation table from 1 to 10

    Example
    -------
    >>> multiple_table(74)
    1 * 74 = 74
    2 * 74 = 148
    3 * 74 = 222
    4 * 74 = 296
    5 * 74 = 370
    6 * 74 = 444
    7 * 74 = 518
    8 * 74 = 592
    9 * 74 = 666
    10 * 74 = 740
    >>> multiple_table(2)
    1 * 2 = 2
    2 * 2 = 4
    3 * 2 = 6
    4 * 2 = 8
    5 * 2 = 10
    6 * 2 = 12
    7 * 2 = 14
    8 * 2 = 16
    9 * 2 = 18
    10 * 2 = 20
    >>> multiple_table(-25)
    1 * -25 = -25
    2 * -25 = -50
    3 * -25 = -75
    4 * -25 = -100
    5 * -25 = -125
    6 * -25 = -150
    7 * -25 = -175
    8 * -25 = -200
    9 * -25 = -225
    10 * -25 = -250
    """

    # Use string format to iterate through a range 1 to 10
    return print('\n'.join( # join string characters using "\n"
        f'{i} * {num} = {i * num}' for i in range(1, 11)))
