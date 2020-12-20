# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def is_valid_braces2(input_str):
    """
    Write a function that takes a string of braces, and determines if
    the order of the braces is valid. It should return true if the
    string is valid, and false if it's invalid. All input strings will
    be nonempty, and will only consist of parentheses, brackets and
    curly braces: ()[]{}

    Parameters
    ----------
    input_str: {str} nonempty string of braces

    Returns
    -------
    {bool}: True if a string of braces is considered valid, all braces
    are matched with the correct brace.

    Example
    -------
    >>> is_valid_braces2("(c(b(a)))(d)")
    True
    >>> is_valid_braces2("(f)ipkcgkp)gisuxcob(ubpamo(oaa))(j)()l")
    False
    >>> is_valid_braces2("o(d(mj(em)c)ojkdbnppk)jbnhra")
    True
    """

    braces = {"(": ")"} # create dictionary of brace
    stack = [] # add complete braces to stack
    for character in input_str:
        if character in braces.keys(): # check for open braces
            stack.append(character)
        elif character in braces.values(): # check for closing braces
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
            else:
                pass
        else: # skip all non parentheses
            pass
    return len(stack) == 0 # check if any remaining open braces
