# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-06

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import numpy as np # can also use traversal as an alternative

def array_combo(input_array):
    """
    Given an array of arrays and your task will be to return the number
    of unique arrays that can be formed by picking exactly one element
    from each subarray

    Parameters
    ----------
    input_array: {list} list of lists, each list has integers

    Returns
    -------
    {int}: count of unique arrays

    Example
    -------
    >>> array_combo([[5, 4, 3, 1, 9, 6, 2, 3], [5, 4, 3, 1, 9, 6, 2, 3], [5, 4, 3, 1, 9, 6, 2, 3]])
    343
    >>> array_combo([[4, 2, 2, 4, 9, 2, 7, 3, 3, 5, 6, 2, 3, 8, 4, 6], [4, 2, 2, 4, 9, 2, 7, 3, 3, 5, 6, 2, 3, 8, 4, 6], [4, 2, 2, 4, 9, 2, 7, 3, 3, 5, 6, 2, 3, 8, 4, 6], [4, 2, 2, 4, 9, 2, 7, 3, 3, 5, 6, 2, 3, 8, 4, 6]])
    4096
    >>> array_combo([[0, 1, 9, 6, 9], [0, 1, 9, 6, 9]])
    16
    """

    # Optional: use try...except block to handle error conditions

    combo_arr = []

    for i in input_array:
        count = len(set(i))
        combo_arr.append(count)

    return np.prod(combo_arr)
