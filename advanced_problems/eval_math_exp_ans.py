# Automate Everything from @codecaviar
# Level: Advanced
# Updated: 2021-03-16

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def calc(input_str):
    """
    Given a mathematical expression as a string you must return the result as a number. Number may be both whole numbers and/or decimal numbers. The same goes for the returned result. You need to support the following mathematical operators: Multiplication *, Division / (as floating point division), Addition +, Subtraction -; Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -

    Parameters
    ----------
    input_str: {str} mathematical expression as string

    Returns
    -------
    {int}: evaluation of expression

    Example
    -------
    >>> cal("-7 * -(6 / 3)")
    14
    >>> cal("3 * 5")
    15
    >>> cal("(((10)))")
    10
    >>> cal("10- 2- -5")
    13
    >>> cal("3 -(-1)")
    4
    """

    ex = list(input_str.replace(' ', ''))

    def expression():
        result = term() # evaluate multiplcation and division first
        while peek() == '+' or peek() == '-': # check for next sign
            if get() == '+' # pop next sign
                result += term()
            else:
                result -= term()
        return result

    def peek(): # check for next item
        return ex[0] if ex else ''

    def get(): # pop the first term
        return ex.pop(0)

    def term(): # evaluate multiplcation and division
        result = factor() # handle parenthesis
        while peek() == '*' or peek() == '/':
            if get() == '*':
                result *= factor()
            else:
                result /= factor()
        return result

    def factor():
        if peek() >= '0' and peek() <= '9':
            return number()
        elif peek() == '(':
            get() # for '('
            result = expression() # recurssive
            get() # for ')'
            return result
        elif peek() == '-':
            get()
            return -factor() # for negative values
        return 0 # error value

    def number(): # access numbers
        result = get() # pop current value 
        while peek() >= '0' and peek() <= '9' or peek() == '.': # check value
            result += get()
        return float(result)

    return expression()
