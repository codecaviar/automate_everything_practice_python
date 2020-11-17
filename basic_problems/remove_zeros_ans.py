# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-07

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def remove_zeros(n):
    """
    Remove all zeros at the end of a number

    Parameters
    ----------
    n: {int} number with or without trailing zeros

    Returns
    -------
    {int}: new number without trailing zeros, return 0 if n = 0

    Example
    -------
    >>> remove_zeros(9095000)
    9095
    >>> remove_zeros(8480000)
    848
    >>> remove_zeros(2986000)
    2986
    """

    # Optional: use try...except block to handle error conditions

    # Use try-except block to check for trailing zeros
    try: # convert n to string and then back to integer
        return int(str(n).rstrip('0')) # use rstrip to remove character

    except ValueError: # only activates if the try statement has error
        return 0
