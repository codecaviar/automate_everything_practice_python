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

    if num <= 1: # address edge cases
        return False
    elif num <= 3:
        return True
    else:
        # Skip middle 5 numbers in below loop
        if (num % 2 == 0 or num % 3 == 0):
            return False

        count = 5
        while (count * count <= num): #
            if (num % count == 0
                or num % (count + 2) == 0):
                return False
            count += 6

        return True

    # The algorithm can be improved further by observing that all primes are of the form 6k ± 1, with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k ± 1 (Source: https://en.wikipedia.org/wiki/Primality_test)
