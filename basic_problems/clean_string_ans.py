# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def clean_string(input_str):
    """
    Assum "#" is like a backspace, process a string with "#" symbols

    Parameters
    ----------
    input_str: {str} chracters including "#" symbol

    Returns
    -------
    {str}: process a string to apply "#" as backspace

    Example
    -------
    >>> clean_string("#####K<^#g#")
    'K<'
    >>> clean_string("y#1Wg#*#=w%q#&;#9k#U&-l")
    '1W=w%&9U&-l'
    >>> clean_string("V=D####/#C##[#")
    ''
    """

    # Optional: use try...except block to handle error conditions
    new_str = []
    for i in input_str:
        if i == "#" and len(new_str) != 0:
            new_str.pop()
        elif i != "#":
            new_str.append(i)
        else:
            continue
    return ''.join(new_str)
