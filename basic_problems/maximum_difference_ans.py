# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-21

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def max_diff(input_arr):
    """
    Given an array of integers, find the maximum difference
    between any two elements such that larger element
    appears after the smaller integer. Return a negative
    value if the array is sorted in decreasing order and
    return 0 if elements are equal.

    Parameters
    ----------
    input_arr: {list} array with random integer numbers

    Returns
    -------
    {int}: max difference between two elements in array

    Example
    -------
    >>> max_diff([2, 3, 10, 6, 4, 8, 1])
    8
    >>> max_diff([7, 9, 5, 6, 3, 2])
    2
    >>> max_diff([1, 2, 90, 10, 110])
    109
    """

    # Initialize placeholders
    diff = input_arr[1] - input_arr[0] # assumes two elements
    curr_sum = diff
    max_sum = curr_sum

    for i in range(1, len(input_arr) - 1):
        # Calculate the current diff
        diff = input_arr[i + 1] - input_arr[i]
        # Calculate current sum
        if (curr_sum > 0):
            curr_sum += diff
        else:
            curr_sum = diff
        # Update max sum, if needed
        if (curr_sum > max_sum):
            max_sum = curr_sum
        else:
            pass

    return max_sum
