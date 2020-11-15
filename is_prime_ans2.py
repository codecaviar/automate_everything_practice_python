# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-14

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def is_prime(num):
    """
    Given one integer argument, return logical value True or False
    depending on if the integer is prime

    Parameters
    ----------
    num: {int} intger may be positive, negative, or zero

    Returns
    -------
    {bool}: True if n is prime number, else False

    Example
    -------
    >>> is_prime(2)
    True
    >>> is_prime(0)
    False
    >>> is_prime(-1)
    False
    >>> is_prime(451936997)
    True
    >>> is_prime(97105469)
    True
    >>> is_prime(1848408607)
    True
    """

    import math

    # Only one even prime: 2
    if num < 2    : return False
    if num == 2   : return True
    if num %2 == 0: return False

    root = int(math.sqrt(num))

    # Only one even prime, iterate only over the odd numbers
    # Use the following property to improve performance:
    # Every number n that is not prime has at least one prime divisor p
    # such 1 < p < square_root(n)

    for i in range(3, root+1, 2):
        if num % i == 0: return False

    return True
