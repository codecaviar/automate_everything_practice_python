# Automate Everything from @codecaviar
# Level: Intermediate
# Updated: 2020-11-22

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

def binary_search(input_list, input_val):
    """
    Take sorted list of elements, start looking for an element at
    middle of the list; if the search value matches with the middle
    value, complete the search. Otherwise, eleminate half of the list
    by choosing whether to process with the right or left half of the
    list, depending on the value of the item searched. Note the list
    is sorted and works much faster than linear search.

    Parameters
    ----------
    input_list: {list} initial list of elements to be searched
    input_val: {int} value to be searched

    Returns
    -------
    {int}: index of input_val in the input_list

    Example
    -------
    >>> binary_search([2, 7, 19, 34, 53, 72], 72)
    5
    >>> binary_search([8, 11, 24, 56, 88, 131], 51)
    None
    >>> binary_search([15, 18, 20, 90, 84, 35, 92, 45, 76, 36], 18)
    1
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
