# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-13

# Fill each function stub according to the docstring.
# Run tests with command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def max_lists(list1, list2):
    """
    The arguments, list1 and list2, have the same length.
    Return a list which contains, for each index,
    the maximum element of both list at this index.

    Parameters
    ----------
    list1: {list} of numeric values
    list2: {list} of numeric values

    Returns
    -------
    {list}: list of maximum values for each index of list1, list2

    Example
    -------
    >>> max_lists([1, 4, 8], [3, 1, 9])
    [3, 4, 9]
    >>> max_lists([5, 7, 2, 3, 6], [3, 9, 1, 2, 8])
    [5, 9, 2, 3, 8]
    >>> max_lists([6, 7, 8, 9, 10], [11, 12, 13, 14, 15])
    [11, 12, 13, 14, 15]
    """

    # Optional: use try...except block to handle error conditions

    max_list = [] # define a final list to return

    # Use built-in enumerate function to add a counter to an iterable
    for idx1, element1 in enumerate(list1): # return counter and element
        # Compare each element from list1 to element in list2
        if element1 > list2[idx1]: # if greater than
            max_list.append(element1) # append to final list
        else: # if not greather than
            max_list.append(list2[idx1]) # append to final list

    return max_list
