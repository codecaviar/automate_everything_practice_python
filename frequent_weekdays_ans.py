# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-30

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import datetime # need to use datetime library

def frequent_weekdays(year):
    """
    Find the most frequent day(s) of the week in the year (1500 - 4000),
    calendar is Gregorian

    Parameters
    ----------
    year: {int} integer of a given year

    Returns
    -------
    {list}: most frequent day(s) of the week, sorted by the order
            of days of in the week (starts with Monday)

    Example
    -------
    >>> frequent_weekdays(3602)
    ['Tuesday']
    >>> frequent_weekdays(2276)
    ['Saturday', 'Sunday']
    >>> frequent_weekdays(2892)
    ['Tuesday', 'Wednesday']
    """

    # Optional: use try...except block to handle error conditions

    # Create a set of all possible weekday values
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday')

    most_days = sorted( # sort the list
        list( # change a set to a list
            set( # create a set of first and last weekdays in year
                [datetime.date(year, 1, 1).weekday(),
                datetime.date(year, 12, 31).weekday()
                ] # check the end of year to account for leap years
            )
        )
    )

    return [days[i] for i in most_days] # return a list from days
