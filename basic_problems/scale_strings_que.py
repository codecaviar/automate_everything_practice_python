# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2021-06-01

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

def scale_strings(input_str, h, v):
    """
    Given a string of 1+ lines, each substring being 1+ characters long, scale the string based on given whole multipliers.

    e.g. input_str = "abcd\\nefgh\\nijkl\\nmnop\\nqrst\\nuvw"

    Parameters
    ----------
    input_str: {str} string with at least a single line and a single character
    h: {int} horizontal scaling to replicate h time each character of the string, not include the '\\n' character
    v: {int} vertical scaling to replicate v times each line of the string

    Returns
    -------
    {str}: string that has been scaled based on the h and v parameters

    Example
    -------
    >>> scale_strings("YVjosW\\nHGhKGZ\\nLHNMLm\\nJtcWCj\\ngVtjyk\\nOJBkOK", 2, 2)
    'YYVVjjoossWW\\nYYVVjjoossWW\\nHHGGhhKKGGZZ\\nHHGGhhKKGGZZ\\nLLHHNNMMLLmm\\nLLHHNNMMLLmm\\nJJttccWWCCjj\\nJJttccWWCCjj\\nggVVttjjyykk\\nggVVttjjyykk\\nOOJJBBkkOOKK\\nOOJJBBkkOOKK'

    >>> scale_strings("CG\\nla", 2, 3)
    'CCGG\\nCCGG\\nCCGG\\nllaa\\nllaa\\nllaa'

    >>> scale_strings("cjqi\\nYKOw\\nmtqz\\nLwBh", 3, 4)
    'cccjjjqqqiii\\ncccjjjqqqiii\\ncccjjjqqqiii\\ncccjjjqqqiii\\nYYYKKKOOOwww\\nYYYKKKOOOwww\\nYYYKKKOOOwww\\nYYYKKKOOOwww\\nmmmtttqqqzzz\\nmmmtttqqqzzz\\nmmmtttqqqzzz\\nmmmtttqqqzzz\\nLLLwwwBBBhhh\\nLLLwwwBBBhhh\\nLLLwwwBBBhhh\\nLLLwwwBBBhhh'
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
