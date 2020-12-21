# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-21

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def move_zeros(input_arr):
    """
    Given an array of random numbers, push all the zero's of
    a given array to the end of the array. The order of all
    other elements should be the same.

    Parameters
    ----------
    input_arr: {list} array with random integer numbers

    Returns
    -------
    {list}: new array with zero's at the end of the array

    Example
    -------
    >>> move_zeros([1, 2, 0, 4, 3, 0, 5, 0])
    [1, 2, 4, 3, 5, 0, 0, 0]
    >>> move_zeros([1, 2, 0, 0, 0, 3, 6])
    [1, 2, 3, 6, 0, 0, 0]
    >>> move_zeros([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])
    [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0]
    """

    count = 0 # count the non-zero elements
    # Traverse the array
    # If element is non-zero, then replace the element at
    # index count with this element
    for i in range(len(input_arr)):
        if input_arr[i] != 0:
            input_arr[count] = input_arr[i]
            count += 1 # increment count
    # Now all non-zero elements shift to front and count is
    # set to index of first 0, make all elements 0 to end
    while count < len(input_arr):
        input_arr[count] = 0
        count += 1

    return input_arr
