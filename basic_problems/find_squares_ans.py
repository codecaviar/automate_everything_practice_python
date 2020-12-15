# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def find_squares(lng, wdth):
    """
    You can cut a given "true" rectangle into squares ("true" rectangle
    meaning that the two dimensions are different)

    Parameters
    ----------
    lng: {int} positive integer for length of rectnagle
    wdth: {int} positive integer for width of rectangle

    Returns
    -------
    {list}: return array of all squares

    Example
    -------
    >>> find_squares(6250, 250)
    [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]
    >>> find_squares(14, 20)
    [14, 6, 6, 2, 2, 2]
    >>> find_squares(1597, 88)
    [88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 13, 13, 13, 13, 13, 13, 10, 3, 3, 3, 1, 1, 1]
    """

    if lng == wdth: # check if rectangle is already a square
        return None
    if lng < wdth: # check if rectangle is long or wide
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth # update length after removing perfect squares
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res
