# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

def pig_latin2(text):
    """
    1) The word starts with a vowel(a,e,i,o,u) -> return the original
    string plus "way".
    2) The word starts with a consonant -> move
    consonants from the beginning of the word to the end of the word
    until the first vowel, then return it plus "ay".
    3) The result must be lowercase, regardless of the case of the
    input. If the input string has any non-alpha characters, the
    function must return None, null, Nothing.
    4) The function must also handle simple random strings and not just
    English words.
    5) The input string has no vowels -> return the original string
    plus "ay".

    Parameters
    ----------
    text: {str} original word before applying pig lating rules

    Returns
    -------
    {str}: word after applying pig latin rules

    Example
    -------
    >>> pig_latin2("TIRedjePACCSHOjedeUN")
    'iredjepaccshojedeuntay'
    >>> pig_latin2("TIMOCCjatrJEJAub")
    'imoccjatrjejaubtay'
    >>> pig_latin2(tiTITHErdsch")
    'ititherdschtay'
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
