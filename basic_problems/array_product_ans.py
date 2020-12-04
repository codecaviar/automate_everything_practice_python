# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def array_product(input_array):
    """
    Given a multi-dimensional array containing 2 or more sub-arrays of
    integers, find the maximum product that can be formed by taking
    any one element from each sub-array.

    Parameters
    ----------
    input_array: {list} list of lists, each list contains an equal
        number of integers (greather than, less than, or equal to 0)

    Returns
    -------
    {int}: maximum product by selecting a single number from each array

    Example
    -------
    >>> array_product([[15, -9, -18, -18], [5, 6, 3, -1]])
    90
    >>> array_product([[3, -15, 11], [11, -13, -3], [2, -4, 9, 11]])
    2145
    >>> array_product([[-5, 3, 18], [2, -10, -4, 16, -17], [9, 6, 3], [15, -2, 0, 8, -12], [-12, -19]])
    784890
    """

    result = input_array[0] # set result as the first sub-array
    for num_arr in range(1, len(input_array)): # iterate array length
        result = [x * y for x in result for y in input_array[num_arr]]
        # multiple all combinations of each element in all arrays
    return max(result)
