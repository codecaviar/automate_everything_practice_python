# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def pascal_triangle(n):
    """
    In mathematics, Pascal's triangle is a triangular array of the
    binomial coefficients expressed with formula (n k) = n!/(n-k)!,
    where n denotes a row of the triangle, and k is a position of a
    term in the row.

    Parameters
    ----------
    n: {int} given a depth (row) in the triangle

    Returns
    -------
    {list}: return n top rows flattened into a 1D list

    Example
    -------
    >>> pascal_triangle(8)
    [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1, 1, 6, 15, 20, 15, 6, 1, 1, 7, 21, 35, 35, 21, 7, 1]
    >>> pascal_triangle(10)
    [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1, 1, 6, 15, 20, 15, 6, 1, 1, 7, 21, 35, 35, 21, 7, 1, 1, 8, 28, 56, 70, 56, 28, 8, 1, 1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    >>> pascal_triangle(1)
    [1]
    """

    result = []
    for line in range(0, n): # iterate through every line
        for i in range(0, line + 1):
            # Every line has number of integers equal to line number
            result.append(binomial_coeff(line, i))
    return result

def binomial_coeff(n, k):
    """
    Every entry in a line is value of a Binomial Coefficient.
    The value of ith entry in line number line is C(line, i)

    C(n, k) = n! / (n-k)! * k!
    C(n, k) = [n * (n-1) * .... * (n-k+1)] / [k * (k-1) * .... * 1]

    Parameters
    ----------
    n: {int} given a depth (row) in the triangle
    k: {int} given a position of a term in the row

    Returns
    -------
    {int}: coefficient for nth row, kth term in row

    Example
    -------
    >>> binomial_coeff(5, 1)
    5
    >>> binomial_coeff(7, 3)
    35
    >>> binomial_coeff(20, 10)
    184756
    """
    res = 1
    if (k > n - k): # check if k is greather than difference
        k = n - k # set k to the difference
    else:
        pass
    for i in range(0, k): # apply simplified bionomial coeff function 
        res = res * (n - i)
        res = res // (i + 1)
    return res
