# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-16

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def in_asc_order(arr):
    """
     An array is said to be in ascending order if there are no two
     adjacent integers where the left integer exceeds the right integer
     in value. Note that array of 1 integer is considered to be sorted
     in ascending order since all (zero) adjacent pairs of integers
     satisfy the condition that the left integer does not exceed the
     right integer in value.

    Parameters
    ----------
    arr: {list} array of integers as input

    Returns
    -------
    {bool}: returns True if array is in ascending order

    Example
    -------
    >>> in_asc_order([57874, 56166, 57169, 10301, 85376, 75250, 31129, 84337, 2977, 81229, 2261, 51729, 15621, 62449, 76099, 53857, 25564, 48125, 6933, 18197])
    False
    >>> in_asc_order([61176, 61974, 82741, 5245, 79254, 93417, 37076, 4628, 63838, 68863, 33146, 30180, 67498, 22423, 27136, 40276, 47355, 19341, 62540, 81604])
    False
    >>> in_asc_order([82, 5919, 20646, 22840, 27611, 37285, 37726, 38706, 39468, 43503, 47237, 53192, 60451, 61797, 70956, 75719, 78366, 89623, 91616, 97744])
    True
    """

    # Optional: use try...except block to handle error conditions

    for i in range(1, len(arr)):
        if arr[i-1] <= arr[i]:
            continue
        else:
            return False

    return True
