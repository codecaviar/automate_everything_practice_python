# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-24

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def find_same_arr(input_arr):
    """
    Given a two-dimensional array, return a new array which
    carries only those arrays from the original, which were
    not empty and whose items are all of the same type.

    Parameters
    ----------
    input_arr: {list} list of lists of various lengths and with different element types

    Returns
    -------
    {list}: list of lists with only same arrays

    Example
    -------
    >>> find_same_arr([[88, 49, 'srkk', 'edev', 'qayd', 635, '', 206, 7, 'lamy'], [181, 999, 965, 542, 552, 205, 295, 222, 672, 24], [887, 387, 922, 976, 725], ['sfpg', 910], [], ['xsyl', '', ''], ['triq', 130, 'oxgl', 'qtmf', 'dcdm', 316, 801, 'owlq'], [108, '', 266, 'ucvw', '', 748], ['lzkf', 'wwuj', 'klez', 'zicr', 'sbcc'], ['gtyg', 'vqnq', '', 'kebc'], [54, 308], [212, 179, 93], [791, 972], ['vtel', 'mumr', 'wqrp', 543, '', 'ogql']])
    [[181, 999, 965, 542, 552, 205, 295, 222, 672, 24], [887, 387, 922, 976, 725], ['xsyl', '', ''], ['lzkf', 'wwuj', 'klez', 'zicr', 'sbcc'], ['gtyg', 'vqnq', '', 'kebc'], [54, 308], [212, 179, 93], [791, 972]]
    >>> find_same_arr([[], [], [886, '', '', 'djqn', 29], [], [378, 93, 87, 54, 8, 641, 610, 435, 494], ['dezr', 'ndxf'], [], ['ggkj', 'abwh'], ['', 'gncy', 'khjo', 'mnip', 'liue', '', '', 'gtta', 'jygl'], ['zqvk', '', 'cajj', '', '', 'neui'], [], ['dhbi', 457, 'afpd', 'fckq', 347, 796, 533, '', 'arem', 764], [916, 533, 950, 'nvzf'], [169, 156, 149, 854, 55, 830, 2]])
    [[378, 93, 87, 54, 8, 641, 610, 435, 494], ['dezr', 'ndxf'], ['ggkj', 'abwh'], ['', 'gncy', 'khjo', 'mnip', 'liue', '', '', 'gtta', 'jygl'], ['zqvk', '', 'cajj', '', '', 'neui'], [169, 156, 149, 854, 55, 830, 2]]
    >>> find_same_arr([[], [100, 662, 822, 118], ['fgda', '', 'pyyg', 'nyed', 'trqf', 'jsfz'], [913, 383, 679], [866, 154, 627], [], ['', '', '', 'ztca', '', 'cxkp', 'ijer', 'dtol'], ['muhp', 401, 472, 'bmhv', 'eowi', 'vuwh'], ['rsci', 908, 930, 'livq', 'inze', 460, 879, 'tsni', ''], ['', 'mbwh', '', 737, 529, 'ebcy'], [740, 15, 948, 535, 'bonz'], ['xfnr', 18, 510, 'tjti', 'mrol', 'bqao'], ['hnyc', 'rdgt', 492]])
    [[100, 662, 822, 118], ['fgda', '', 'pyyg', 'nyed', 'trqf', 'jsfz'], [913, 383, 679], [866, 154, 627], ['', '', '', 'ztca', '', 'cxkp', 'ijer', 'dtol']]
    """

    # Use map to identify unique values
    return [a for a in input_arr if len(set(map(type,a)))==1]
