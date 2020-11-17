# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-30

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def consecutive_num(some_list, num1, num2):
    """
    Check where two integers num1 and num2 are consecutive in the list,
    num1 and num2 are both guaranteed to be in some_list

    Parameters
    ----------
    some_list: {list} random list of integers
    num1: {int} integer to check
    num2: {int} another integer to check

    Returns
    -------
    {bool}: return True if num1 and num2 are consectutive, in either
            order, otherwise return False

    Example
    -------
    >>> consecutive_num([1, 2, 3, 4, 5], 1, 5)
    False
    >>> consecutive_num([1, 4, 5, 3, 2, 7, 6, 23, 76, 11, 0], 2, 3)
    True
    >>> consecutive_num([952326, -623609, -432119, -757494, -146675, -800880, 25493, 15771, 120356, 561829, 320168, -165330, -614993, 324279, -385864, -260167, 965311, -733246, -342973, -528188, 249282, 845640, -12087, -917808, -449198, -645803, -533927, 826346, -162196, 411244, 918510, -216466, 905198, -650003, 206578, 329846, -311688], 329846, 320168)
    False
    """

    # Optional: use try...except block to handle error conditions

    index1 = some_list.index(num1) # find the index of num1 in some_list
    index2 = some_list.index(num2) # find the index of num2
    # num1 and num2 can be consecutive in either order num1 then num2
    # or num2 then num1, both are correct
    return index1 == index2 - 1 or index2 == index1 - 1
