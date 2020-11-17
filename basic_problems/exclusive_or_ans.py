# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-12

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def exclusive_or(a, b):
    """
    Evaluate two booleans and returns True if exactly one of the
    two expressions are True, returns False otherwise

    Parameters
    ----------
    a: {bool} one boolean
    b: {bool} another boolean

    Returns
    -------
    {bool}: True if exactly one of the two expressions are True

    Example
    -------
    >>> exclusive_or(False, False)
    False
    >>> exclusive_or(True, False)
    True
    >>> exclusive_or(False, True)
    True
    >>> exclusive_or(True, True)
    False
    """

    # Optional: use try...except block to handle error conditions

    return a + b == 1 # True is 1 and False is 0
    # Make a conditional statement to check addition of two booleans
