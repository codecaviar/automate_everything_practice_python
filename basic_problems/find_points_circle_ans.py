# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

from math import sqrt # use squareroot to calculate circle

def find_points_circle(rad):
    """
    You have the radius of a circle with the center in point (0,0).
    Write a function that calculates  number of points in the circle
    where (x,y) - the cartesian coordinates of the points are integers.

    Parameters
    ----------
    rad: {int} radius of circle with center at (0,0)

    Returns
    -------
    {int}: total number of points that are integers

    Example
    -------
    >>> find_points_circle(99)
    30757
    >>> find_points_circle(17)
    901
    >>> find_points_circle(1)
    5
    """

    point = sum(int(sqrt(rad * rad - x * x)) # find points in circle
        for x in range(0, rad+1)) * 4 + 1 # multiple for quadrants

    return point
