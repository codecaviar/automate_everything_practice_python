# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def sum_two_array(array1, array2):
    """
    Takes two arrays consisting of integers, and returns the sum of
    those two arrays, where [3,2,9] = '3' + '2' + '9' = 329.
    If both arrays are empty, return an empty array.
    If first index is a negative number, treat whole number as negative.

    Parameters
    ----------
    array1: {list} intgers, possible negative number in first element
    array2: {list} intgers, possible negative number in first element

    Returns
    -------
    {list}: Returns the sum of those two arrays, with elements as
        integers in a list

    Example
    -------
    >>> sum_two_array([6], [3, 4, 7])
    [3, 5, 3]
    >>> sum_two_array([], [9, 0])
    [9, 0]
    >>> sum_two_array([], [])
    []
    >>> sum_two_array([-8, 5, 9, 8, 0, 6], [6, 0, 2, 9])
    [-8, 5, 3, 7, 7, 7]
    >>> sum_two_array([-5, 4, 5, 5], [4])
    [-5, 4, 5, 1]
    """

    # Optional: use try...except block to handle error conditions

    if not array1:
        return array2
    elif not array2:
        return array1
    else:
        num = sum(map(lambda x: int(''.join(map(str, x))),
            [array1, array2]))
        lst = list(map(int, str(abs(num))))
        if num < 0:
            lst[0] *= -1
        else:
            pass
        return lst
