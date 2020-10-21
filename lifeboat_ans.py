# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-17

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def lifeboat(shark_dist, shark_speed, boat_dist, swim_speed, harpoon):
    """
    Return whether or not a surfer can make it to the lifeboat
    before the shark catches up to the surfer swimming in a straight
    line towards the lifeboat

    Parameters
    ----------
    shark_dist: {int} distance in meters between shark and lifeboat
    shark_speed: {int} how fast the shark can move in meters/second
    boat_dist: {int} distance in meters between surfer and lifeboat
    swim_speed: {int} how fast surfer can swim in meters/second
    harpoon: {bool} if true, half the swimming speed of the shark

    Returns
    -------
    {bool}: surfer is shark bait if False, otherwise alive if True

    Example
    -------
    >>> lifeboat(50, 1, 3, 4, False)
    False
    >>> lifeboat(20, 150, 2, 10.0, True)
    False
    >>> lifeboat(8, 100, 4, 10, True)
    True
    """

    # Optional: use try...except block to handle error conditions

    # Check whether or not the surfer has a harpoon
    if harpoon:
        shark_speed = shark_speed / 2 # divide shark_speed in half
    else:
        None

    # Calculate shark swim time
    shark_time = shark_dist / shark_speed

    # Calculate surfer swim time
    surfer_time = boat_dist / swim_speed

    return surfer_time > shark_time
