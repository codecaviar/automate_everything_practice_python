# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def frequency_sort(arr):
    """
    Sort elements in an array by decreasing frequency of elements,
    if two elements have the same frequency, sort by increasing value

    Parameters
    ----------
    arr: {list} array of various frequency of integers

    Returns
    -------
    {list}: sort by highest frequency to lowest frequency

    Example
    -------
    >>> frequency_sort([32, 19, 26, 33, 47, 12, 25, 45, 37, 40, 3, 35, 35, 10, 19, 23, 30, 24, 23, 25, 29, 13, 23, 32, 21, 35, 21, 49, 30, 7, 21, 33, 37, 16, 4, 37, 0, 28, 25, 40, 0])
    [21, 21, 21, 23, 23, 23, 25, 25, 25, 35, 35, 35, 37, 37, 37, 0, 0, 19, 19, 30, 30, 32, 32, 33, 33, 40, 40, 3, 4, 7, 10, 12, 13, 16, 24, 26, 28, 29, 45, 47, 49]
    >>> frequency_sort([40, 9, 9, 20, 21, 44, 18, 34, 36, 20, 20, 32, 19, 28])
    [20, 20, 20, 9, 9, 18, 19, 21, 28, 32, 34, 36, 40, 44]
    >>> frequency_sort([27, 26, 47, 34, 29, 11, 13, 48, 10, 39, 14, 27, 15, 30, 20, 18, 0, 16, 37, 8, 45, 0, 3, 39, 12, 1, 5, 23, 43, 42, 30, 42, 4, 11, 41, 41, 38, 42, 17, 31, 22, 3, 43, 9, 18])
    [42, 42, 42, 0, 0, 3, 3, 11, 11, 18, 18, 27, 27, 30, 30, 39, 39, 41, 41, 43, 43, 1, 4, 5, 8, 9, 10, 12, 13, 14, 15, 16, 17, 20, 22, 23, 26, 29, 31, 34, 37, 38, 45, 47, 48]
    """

    # Optional: use try...except block to handle error conditions
    counts = [] # create a count of each element
    for i in set(arr):
        counts.append((arr.count(i), i)) # tuple with count and element
    # Sort the list of tuples by reverse of count and value
    double_sort = sorted(counts, key=lambda tup: (-tup[0], tup[1]))
    # Rebuild
    temp = [[double_sort[i][1]]*double_sort[i][0] for i in range(0, len(double_sort))] # build a list of lists
    return [x for y in temp for x in y] # recreate single list

    # Simpler solution:
    # return sorted(arr, key= lambda x: (-arr.count(x), x))
