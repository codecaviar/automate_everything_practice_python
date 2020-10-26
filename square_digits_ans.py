# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-25

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def square_digits(num):
    """
    Square every integer of a number and concatenate the results together as a new integer

    Parameters
    ----------
    num: {int} input number that needs to be transformed

    Returns
    -------
    {int}: output number after squaring every integer and concatenating the results together

    Example
    -------
    >>> square_digits(7934)
    4981916
    >>> square_digits(8514)
    6425116
    >>> square_digits(5382)
    259644
    """

    # Optional: use try...except block to handle error conditions

    new_num = "" # define a blank string

    for i in str(num): # iterate through original integer as a string
        new_num += str(int(i) ** 2) # square each integer

    return int(new_num) # convert final concatenated result as integer 
