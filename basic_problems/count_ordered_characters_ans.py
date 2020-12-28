# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-27

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

from collections import Counter

def count_ordered(input_str):
    """
    Count the number of occurrences of each character and return it as
    a list of tuples in order of appearance.
    For empty output return an empty list.

    Parameters
    ----------
    input_str: {str} alphabet characters in a string format

    Returns
    -------
    {list}: array of tuples

    Example
    -------
    >>> count_ordered("abracadabra")
    [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
    >>> count_ordered("ASDFGHJKertyujikxdcfvghjcvbhnjmkswedrftyuioawsertyui1q234567890!@#$ER%^&*()sdfgthyujdfg@#$%^&*(QWERTYUISDFGHJKZXCVBN@#E$%T^Y&U*()ERTYUISDFGHJXCFVGHJERTYUIertyuisdfghjkerty7u8iqwertyuiopxdcfghjkicvgbhnj2345678i9o0!@#$%^&*(23456789))")
    [('A', 1), ('S', 3), ('D', 3), ('F', 4), ('G', 4), ('H', 4), ('J', 4), ('K', 2), ('e', 6), ('r', 6), ('t', 7), ('y', 7), ('u', 7), ('j', 7), ('i', 8), ('k', 4), ('x', 2), ('d', 6), ('c', 4), ('f', 6), ('v', 3), ('g', 6), ('h', 6), ('b', 2), ('n', 2), ('m', 1), ('s', 4), ('w', 3), ('o', 3), ('a', 1), ('1', 1), ('q', 2), ('2', 3), ('3', 3), ('4', 3), ('5', 3), ('6', 3), ('7', 4), ('8', 4), ('9', 3), ('0', 2), ('!', 2), ('@', 4), ('#', 4), ('$', 4), ('E', 5), ('R', 4), ('%', 4), ('^', 4), ('&', 4), ('*', 4), ('(', 4), (')', 4), ('Q', 1), ('W', 1), ('T', 4), ('Y', 4), ('U', 4), ('I', 3), ('Z', 1), ('X', 2), ('C', 2), ('V', 2), ('B', 1), ('N', 1), ('p', 1)]
    >>> count_ordered("qwertyuiopasedrfgthyjukixdcfvgbhnjQWERTYUISDFGHJXCVGBHN!@#$%^&*(@W#$%T^Y*I(#$%^&*(sedrftgyh234567y23456782345678sDERFTGYUEDRTYUDFGHJKDFGHJKcvfgbhnjmkxcfvgbhnjsdfghyujqwertyuiop)(*&^%$(*&^%R$EIUYTRIUYTRFkijuhygtiuytriuytgfrdkjhgkjhgfoiuytr9i8u7y6trujhy))))")
    [('q', 2), ('w', 2), ('e', 4), ('r', 8), ('t', 9), ('y', 12), ('u', 10), ('i', 8), ('o', 3), ('p', 2), ('a', 1), ('s', 4), ('d', 5), ('f', 8), ('g', 10), ('h', 10), ('j', 9), ('k', 5), ('x', 2), ('c', 3), ('v', 3), ('b', 3), ('n', 3), ('Q', 1), ('W', 2), ('E', 4), ('R', 6), ('T', 6), ('Y', 6), ('U', 5), ('I', 4), ('S', 1), ('D', 5), ('F', 5), ('G', 5), ('H', 4), ('J', 3), ('X', 1), ('C', 1), ('V', 1), ('B', 1), ('N', 1), ('!', 1), ('@', 2), ('#', 3), ('$', 5), ('%', 5), ('^', 5), ('&', 4), ('*', 5), ('(', 5), ('2', 3), ('3', 3), ('4', 3), ('5', 3), ('6', 4), ('7', 4), ('8', 3), ('K', 2), ('m', 1), (')', 5), ('9', 1)]
    """

    return list(Counter(input_str).items())

    # Alternate solution:
    # list(dict.fromkeys([(i, inp.count(i)) for i in input_str]))
