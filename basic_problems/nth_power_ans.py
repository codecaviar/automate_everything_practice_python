# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def nth_power(array, n):
    """
    Input is a list of positive numbers and a number N.
    You should find the N-th power of the element in the array with
    the index N. If N is outside of the array, then return -1.

    Parameters
    ----------
    array: {list} of postive numeric values
    n: {int} a positive intger

    Returns
    -------
    {int}: an integer that is the n-th power of the n element
           or the value -1 if n is outside of the array

    Example
    -------
    >>> nth_power([1, 2, 3, 4],2)
    9
    >>> nth_power([1, 3, 10, 100], 3)
    1000000
    >>> nth_power([1, 2], 2)
    -1
    """

    try: # use try...except to check n is inside of the input array
        return array[n]**n # calculate the n-th power of n-th element

    except:
        return -1 # if error is raised, return default value of -1
