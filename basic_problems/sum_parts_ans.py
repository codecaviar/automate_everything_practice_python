# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-28

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

from functools import reduce # option to use reduce from functools

def sum_parts(input_list):
    """
    Example:
    input_list = [0, 1, 3, 6, 10]

    input_list = [0, 1, 3, 6, 10]
    input_list = [1, 3, 6, 10]
    input_list = [3, 6, 10]
    input_list = [6, 10]
    input_list = [10]
    input_list = []

    total_sum = [20, 20, 19, 16, 10, 0]

    Parameters
    ----------
    input_list: {list} array of integers

    Returns
    -------
    {list}: sum of parts as defined above

    Example
    -------
    >>> sum_parts([1, 5, 10, 10, 2, 9, 9])
    [46, 45, 40, 30, 20, 18, 9, 0]
    >>> sum_parts([8, 8, 10, 6, 10, 2, 8, 7, 7])
    [66, 58, 50, 40, 34, 24, 22, 14, 7, 0]
    >>> sum_parts([7, 10, 8, 8, 1, 1, 3, 3])
    [41, 34, 24, 16, 8, 7, 6, 3, 0]
    """

    result = [sum(input_list)] # create initial
    for item in input_list: # iterate through the list of elements
        result.append(result[-1]-item) # subtract the last sum 
    return result
