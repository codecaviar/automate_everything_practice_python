# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def square_or_rectangle(l, w):
    """
    Given the length and width of a 4-sided polygon, return the area
    if it's a square, but return the perimeter if it's a rectangle

    Parameters
    ----------
    l: {int} length in inches
    w: {int} width in inches

    Returns
    -------
    {int}: area or perimeter in inches

    Example
    -------
    >>> square_or_rectangle(2, 2)
    4
    >>> square_or_rectangle(4802, 8402)
    26408
    >>> square_or_rectangle(21602, 37802)
    118808
    """

    # Optional: use try...except block to handle error conditions

    if l == w: # square has equal length and width
        polygon = l * w # calculate area
    else:
        polygon = (l + w) * 2 # calculate perimeter

    return polygon # return correct answer from conditional statement
