# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-13

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def get_diagonal(mat):
    """
    Given a matrix encoded as a 2 dimensional python list, return a
    list containing all the values in the diagonal starting at the
    index 0,0.

    Parameters
    ----------
    mat: 2 dimensional list ({list} of {list} of numeric values)

    Returns
    -------
    {list}: values in the diagonal

    Example
    -------
    E.g.
    mat = [[1, 2], [3, 4], [5, 6]]
    | 1  2 |
    | 3  4 |
    | 5  6 |
    get_diagonal(mat) => [1, 4]

    You may assume that the matrix is nonempty.

    >>> get_diagonal([[1, 2], [3, 4], [5, 6]])
    [1, 4]
    >>> get_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 5, 9]
    >>> get_diagonal([[5, 4, 3, 2, 1], [1, 2, 3, 4, 5]])
    [5, 2]
    """

    # Use list comprehension to return a list
    # Find minimum of number of rows in matrix len(mat) and
    # number of columns len(mat[0]) given that rows have the
    # same number of columns
    diagonal = [mat[i][i] for i in range(min(len(mat[0]), len(mat)))]

    return diagonal
