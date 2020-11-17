# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-07

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def planet_name(id):
    """
    Return the name of the planet for our solar system, with numberic
    order based on distance from the sun

    Parameters
    ----------
    id: {int} number for the planet location

    Returns
    -------
    {string}: name of planet, in title format, return "New" otherwise

    Example
    -------
    >>> planet_name(2)
    'Venus'
    >>> planet_name(4)
    'Mars'
    >>> planet_name(50)
    'New'
    """

    # Optional: use try...except block to handle error conditions

    # Define a dictionary with the planet location as keys and
    # planet names as values
    name_dict = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"
    }

    return name_dict.get(id, "New") # get method will return default
