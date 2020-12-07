# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def draw_stairs(n):
    """
    Given a number n, draw stairs using the letter "I",
    n tall and n wide, with the tallest step in the top left.

    Parameters
    ----------
    n: {int} ...

    Returns
    -------
    {...}: ...

    Example
    -------
    >>> draw_stairs(3)
    I
     I
      I
    >>> draw_stairs(10)
    I
     I
      I
       I
        I
         I
          I
           I
            I
             I
    >>> draw_stairs(15)
    I
     I
      I
       I
        I
         I
          I
           I
            I
             I
              I
               I
                I
                 I
                  I
    """

    result = ""
    for i in range(1, n): # iterate through number of stairs
        result += "I\n" + " " * i # pad with additional spaces for each
    return print("{}{}".format(result, "I")) # end with final stair
