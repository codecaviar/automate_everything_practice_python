# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def combine_triple(one, two, three):
    """
    Given three input strings, take the first letter of all the inputs
    and group them next to each other in a single string

    Parameters
    ----------
    one: {str} first input string
    two: {str} second input string
    three: {str} third input string

    Returns
    -------
    {str}: combined strings

    Example
    -------
    >>> combine_triple("aaaaaa", "bbbbbb", "cccccc")
    'abcabcabcabcabcabc'
    >>> combine_triple("byCS5hG9", "1RKMCWlV", "6c7THY4R")
    'b16yRcCK7SMT5CHhWYGl49VR'
    >>> combine_triple("GsVhf10pXOsMeDIf", "osexkl6aP4OoQbrH", "vnaKV1WIb7T2o4Rm")
    'GovssnVeahxKfkV1l106WpaIXPbO47sOTMo2eQoDb4IrRfHm'
    """

    return ''.join(''.join(a) for a in zip(one, two, three))
