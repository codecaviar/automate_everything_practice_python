# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-08

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import math # use ceil method

def movie_ticket(card, ticket, prcnt):
    """
    A cinema has two ticket systems: A and B
    System A : one buys a ticket every time
    System B : one buys a card and a first ticket for percent times the
    ticket price, then for each additional ticket one pays percent
    times the price paid for the previous ticket.

    How many times one must go to the cinema so that the final result
    of System B, when rounded up to the next dollar, will be cheaper
    than System A?

    Parameters
    ----------
    card: {int} price of card
    ticket: {int} normal price of a ticket
    prcnt: {float} fraction of what one paid for the previous ticket

    Returns
    -------
    {int}: number of trips to cinema, ceil(System B) < System A

    Example
    -------
    >>> movie_ticket(775435, 49, 0.12)
    15826
    >>> movie_ticket(810245, 38, 0.29)
    21323
    >>> movie_ticket(358356, 10, 0.1)
    35836
    """

    num = 0
    price_a = 0
    price_b = card # set price b as max for card

    while math.ceil(price_b) >= price_a: # condition to check
        num += 1
        price_a += ticket # apply rule for price a
        price_b += ticket * (prcnt ** num) # apply rule for price b

    return num
