# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-13

# Fill each function stub according to the docstring.
# Run tests with command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def merge_dict(d1, d2):
    """
    Return a new dictionary which contains all the keys from d1 and d2
    with their associated values. If a key is in both dictionaries, the
    value should be the sum of the two values.

    Parameters
    ----------
    d1: {dict} with str keys and numeric values
    d2: {dict} with str keys and numeric values

    Returns
    -------
    {dict}: all key and value pairs from both dictionaries

    Example
    -------
    >>> d1 = {"a": 1, "b": 5, "c": 1, "e": 8}
    >>> d2 = {"b": 2, "c": 5, "d": 10, "f": 6}
    >>> merge_dict(d1,d2) == {"a": 1, "b": 7, "c": 6, "d": 10, "e": 8, "f": 6}
    True
    """

    # Optional: use try...except block to handle error conditions

    # Define new dictionary using dict comprehension
    # Use get method to return value of the dictionary item, default 0
    new_dict = {x: d1.get(x, 0) + d2.get(x, 0)
        # Use set to get unique keys
        # Use union to return a set that contains unique keys from both
        for x in set(d1).union(d2)}

    return new_dict
