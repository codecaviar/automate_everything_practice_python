# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-19

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def line_numbers(lines):
    """
    Take a list of strings and returns each line prepended
    by the correct number (starting at 1)

    Parameters
    ----------
    lines: {list} list of strings

    Returns
    -------
    {list}: elements are in the format n: string, note colon and space

    Example
    -------
    >>> line_numbers(['', '', '', '', ''])
    ['1: ', '2: ', '3: ', '4: ', '5: ']
    >>> line_numbers([])
    []
    >>> line_numbers(['6', 'T', 'A', '1', 'z', 'R', 'R', 't', 'M', 'Q', 'L', '3', '7', 't', 'f', 'h', 'Y', '2', 'e', '9', '?', 'f', '@', 'E', 'B', 'x', 'm', 'q', '2', 'R', 'M', 'b', '`', 'Y', ';', 'v', 'o', 'S', '3', 'P', 'T', '<', 'm', 'L', '<', 'M', 'N', 'g', 'r', 'y', 'S', '=', 'Z', 'n', ':', 't', '4', 'c', ':', 'Q', 'j', 'p', 'Q', '@', '`', 'g', 'b', 'Q', 's', 'u', '6', '2', '@', '[', '_', 'W', 'M', 'm', 'F', 't', 'h', 'F', 'v', 'd', 'W', 'w', ']', '9', 'P', 'F', 'w', 'U', 'p', 'R', 'i', 'i', 'i', 'a', '6', 'q'])
    ['1: 6', '2: T', '3: A', '4: 1', '5: z', '6: R', '7: R', '8: t', '9: M', '10: Q', '11: L', '12: 3', '13: 7', '14: t', '15: f', '16: h', '17: Y', '18: 2', '19: e', '20: 9', '21: ?', '22: f', '23: @', '24: E', '25: B', '26: x', '27: m', '28: q', '29: 2', '30: R', '31: M', '32: b', '33: `', '34: Y', '35: ;', '36: v', '37: o', '38: S', '39: 3', '40: P', '41: T', '42: <', '43: m', '44: L', '45: <', '46: M', '47: N', '48: g', '49: r', '50: y', '51: S', '52: =', '53: Z', '54: n', '55: :', '56: t', '57: 4', '58: c', '59: :', '60: Q', '61: j', '62: p', '63: Q', '64: @', '65: `', '66: g', '67: b', '68: Q', '69: s', '70: u', '71: 6', '72: 2', '73: @', '74: [', '75: _', '76: W', '77: M', '78: m', '79: F', '80: t', '81: h', '82: F', '83: v', '84: d', '85: W', '86: w', '87: ]', '88: 9', '89: P', '90: F', '91: w', '92: U', '93: p', '94: R', '95: i', '96: i', '97: i', '98: a', '99: 6', '100: q']
    """

    # Optional: use try...except block to handle error conditions

    if len(lines) == 0:
        result = lines # address edge case of empty string
    else:
        result = [] # enumerate provides count and element
        for count,ele in enumerate(lines):
            result.append(str(count+1) + ": " + ele)

    return result

    # alternative: ['%d: %s' % v for v in enumerate(lines, 1)]
