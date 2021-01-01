# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def remove_vowels(input_str):
    """
    Deal with trolls in comment section by removing all the vowels from
    the trolls' comments, neutralizing the threat

    Parameters
    ----------
    input_str: {str} sentence from comment section

    Returns
    -------
    {str}: sentence without vowels

    Example
    -------
    >>> remove_vowels("No offense but, Your writing is among the worst Ive ever read")
    'N ffns bt, Yr wrtng s mng th wrst v vr rd'
    >>> remove_vowels("What are you, a communist?")
    'Wht r y,  cmmnst?'
    >>> remove_vowels("\t\t._\x0c \t \x0c\x0c U\x0b\x0c\r \x0b\n\r \t\x0b\nw& T\x0cS\n\x0b\t \x0b\t \r\r^\x0c P\t\x0b&\x0c")
    '\t\t._\x0c \t \x0c\x0c \x0b\x0c\r \x0b\n\r \t\x0b\nw& T\x0cS\n\x0b\t \x0b\t \r\r^\x0c P\t\x0b&\x0c'
    """

    return "".join(c for c in input_str if c.lower() not in "aeiou")
