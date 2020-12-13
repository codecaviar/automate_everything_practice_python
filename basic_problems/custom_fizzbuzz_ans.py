# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def custom_fizzbuzz(string_one='Fizz', string_two='Buzz',
                     num_one=3, num_two=5):
    """
    Create custom Fizz-Buzz function, where index of a number divisible
    by 3 and 5 contains 'FizzBuzz', while only 3 contains 'Fizz' and
    only 5 contains 'Buzz'

    Parameters
    ----------
    string_one: {str} default value of 'Fizz'
    string_two: {str} default value of 'Buzz'
    num_one: {int} default value of 3, num_one < num_two
    num_two: {int} default value of 5

    Returns
    -------
    {list}: array, counting from 1 to 100, inluding Fizz Buzz inserts

    Example
    -------
    >>> custom_fizzbuzz()
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
    >>> custom_fizzbuzz('Hey', 'There')
    [1, 2, 'Hey', 4, 'There', 'Hey', 7, 8, 'Hey', 'There', 11, 'Hey', 13, 14, 'HeyThere', 16, 17, 'Hey', 19, 'There', 'Hey', 22, 23, 'Hey', 'There', 26, 'Hey', 28, 29, 'HeyThere', 31, 32, 'Hey', 34, 'There', 'Hey', 37, 38, 'Hey', 'There', 41, 'Hey', 43, 44, 'HeyThere', 46, 47, 'Hey', 49, 'There', 'Hey', 52, 53, 'Hey', 'There', 56, 'Hey', 58, 59, 'HeyThere', 61, 62, 'Hey', 64, 'There', 'Hey', 67, 68, 'Hey', 'There', 71, 'Hey', 73, 74, 'HeyThere', 76, 77, 'Hey', 79, 'There', 'Hey', 82, 83, 'Hey', 'There', 86, 'Hey', 88, 89, 'HeyThere', 91, 92, 'Hey', 94, 'There', 'Hey', 97, 98, 'Hey', 'There']
    >>> custom_fizzbuzz('iDn', 'p', 4, 9)
    [1, 2, 3, 'iDn', 5, 6, 7, 'iDn', 'p', 10, 11, 'iDn', 13, 14, 15, 'iDn', 17, 'p', 19, 'iDn', 21, 22, 23, 'iDn', 25, 26, 'p', 'iDn', 29, 30, 31, 'iDn', 33, 34, 35, 'iDnp', 37, 38, 39, 'iDn', 41, 42, 43, 'iDn', 'p', 46, 47, 'iDn', 49, 50, 51, 'iDn', 53, 'p', 55, 'iDn', 57, 58, 59, 'iDn', 61, 62, 'p', 'iDn', 65, 66, 67, 'iDn', 69, 70, 71, 'iDnp', 73, 74, 75, 'iDn', 77, 78, 79, 'iDn', 'p', 82, 83, 'iDn', 85, 86, 87, 'iDn', 89, 'p', 91, 'iDn', 93, 94, 95, 'iDn', 97, 98, 'p', 'iDn']
    """

    result = list(range(1, 100+1)) # array counting from 1 to 100
    for i in result:
        if i % num_one == 0 and i % num_two == 0: # first check multiple
            result[i-1] = string_one + string_two
        elif i % num_one == 0: # then check single number
            result[i-1] = string_one
        elif i % num_two == 0: # then check other number
            result[i-1] = string_two
        else:
            pass
    return result
