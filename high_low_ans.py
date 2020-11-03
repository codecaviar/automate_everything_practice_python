# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-01

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def high_low(input_string):
    """
    Return the highest and lowest numbers from a string, with at least
    one number in the input string

    Parameters
    ----------
    input_string: {string} space separated numbers, all numbers are
        valid Int32, no need to validate

    Returns
    -------
    {string}: two numbers separated by a single space, highest number
        is listed first in the string

    Example
    -------
    >>> high_low("329 2259 407 4 2648 253 1606 1172 1055 166 1223 633 1779 1994 2674 744 846 2980 -120 130 1404 1997")
    '2980 -120'
    >>> high_low("2215 3206 2697 2241 3203 1823 543 702 2735 2554 947 643 2949 3407 2486 1605 1507 2111 2506 2439 405 2388")
    '3407 405'
    >>> high_low("3388 735 3305 2914 2889 1578 1712 3467 2640 1702 1021 2544 2936 1703 2991 1555 1370 406 2100 1298 2544 1322")
    '3467 406'
    """

    num = [int(x) for x in input_string.split(" ")]

    return "{} {}".format(max(num), min(num))
