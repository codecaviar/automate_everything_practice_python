# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def clock(hrs, mins, secs):
    """
    Convert time in 'hrs' hours, 'mins' minutes and 'secs' seconds after midnight into milliseconds.

    Parameters
    ----------
    hrs: {int} integer representing hours, 0 <= hrs <= 23
    mins: {int} integer representing minutes, 0 <= mins <= 59
    secs: {int} integer representing seconds, 0 <= secs <= 59

    Returns
    -------
    {int}: integer representing milliseconds

    Example
    -------
    >>> clock(0, 1, 1)
    61000
    >>> clock(0, 0, 0)
    0
    >>> clock(1, 0, 0)
    3600000
    """

    # Optional: use try...except block to handle error conditions

    # Convert hours and mins into seconds, then add seconds
    new_time =  (3600 * hrs + 60 * mins + secs) * 1000

    return new_time
