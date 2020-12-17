# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def encode(s, t=str.maketrans("aeiou", "12345")):
    """
    Replace all the lowercase vowels in a given string with numbers
    according to the following pattern:
    a -> 1, e -> 2, i -> 3, o -> 4, u -> 5

    Parameters
    ----------
    s: {str} initial string to encode

    Returns
    -------
    {str}: output string with rules applied

    Example
    -------
    >>> encode("pswyobbztotdtwcydkpg")
    'pswy4bbzt4tdtwcydkpg'
    >>> encode("iurrgqtoldzkogljz")
    '35rrgqt4ldzk4gljz'
    >>> encode("qvnutpokghgzsvzszzdbtnterdlawg")
    'qvn5tp4kghgzsvzszzdbtnt2rdl1wg'
    """
    return s.translate(t)

def decode(s, t=str.maketrans("12345", "aeiou")):
    """
    Replace all the lowercase vowels in a given string with numbers
    according to the following pattern:
    a -> 1, e -> 2, i -> 3, o -> 4, u -> 5

    Parameters
    ----------
    s: {str} initial string with encode rules applied

    Returns
    -------
    {str}: output string undoing encode rules 

    Example
    -------
    >>> dencode("fqxq3n1t21wp4qwmk2cwyj")
    'fqxqinateawpoqwmkecwyj'
    >>> decode("ngchbwpgdd44p42zmj3m2gs1nvd54")
    'ngchbwpgddoopoezmjimegsanvduo'
    >>> dencode("tk4qpstbytjvxxgh41m3ry3hpyptz")
    'tkoqpstbytjvxxghoamiryihpyptz'
    """
    return s.translate(t)
