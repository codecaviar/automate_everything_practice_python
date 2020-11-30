# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def pig_latin(text):
    """
    Move the first letter of each word to the end of it, then add "ay"
    to the end of the word. Leave punctuation marks untouched.

    Parameters
    ----------
    text: {str} original word before applying pig lating rules

    Returns
    -------
    {str}: word after applying pig latin rules

    Example
    -------
    >>> pig_latin("Timeo Danaos et dona ferentes")
    'imeoTay anaosDay teay onaday erentesfay'
    >>> pig_latin("Hic et nunc")
    'icHay teay uncnay'
    >>> pig_latin("Ultima necat")
    'ltimaUay ecatnay'
    """

    word = ""

    for i in text.split(): # split the word into individual letters
        if i.isalpha(): # check if character is a letter
            word += f'{i[1:]}{i[0]}ay ' # create new sentence
        else: # apply pig latin rules
            word += i

    return word.rstrip() # remove extra spaces
