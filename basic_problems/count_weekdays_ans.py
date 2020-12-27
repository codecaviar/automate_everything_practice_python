# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-24

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import datetime # use datetime, weekday

def count_weekdays(year):
    """
    Given a Gregorian year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has
    to be a list of days sorted by the order of days in week (e. g.
    ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday',
    'Sunday']). Week starts with Monday.

    Parameters
    ----------
    year: {int} year to evaluate

    Returns
    -------
    {list}: single element string, weekday with the highest frequency

    Example
    -------
    >>> count_weekdays(1901)
    ['Tuesday']
    >>> count_weekdays(2135)
    ['Saturday']
    >>> count_weekdays(2016)
    ['Friday', 'Saturday']
    """

    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    most_days = sorted(
        list(
            set(
                [datetime.date(year, 1, 1).weekday(),
                datetime.date(year, 12, 31).weekday()
                ]
            )
        )
    )

    return [days[i] for i in most_days]
