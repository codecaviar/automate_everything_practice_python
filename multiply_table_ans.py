# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-12

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def multiply_table(size):
    """
    Create NxN multiplication table, size provided in parameter

    Parameters
    ----------
    size: {int} N value for a NxN multiplcation table

    Returns
    -------
    {list}: list of lists that is of size NxN

    Example
    -------
    >>> multiply_table(5)
    [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
    >>> multiply_table(10)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80], [9, 18, 27, 36, 45, 54, 63, 72, 81, 90], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
    >>> multiply_table(15)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120], [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150], [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165], [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180], [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195], [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196, 210], [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]]
    """

    # Optional: use try...except block to handle error conditions

    # Use list comprehensions to create a list of lists
    # Create inner list based on multiplication of each integer
    new_table = [[i * j for j in range(1, size + 1)]
        for i in range(1, size + 1)] # outer list provides size range

    return new_table
