# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-02

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def score_exam(exam_key, student_ans):
    """
    The two arrays are not empty and are the same length.
    Return the score for the student answers, based on the exam key.
    +4 for correct answers, -1 for incorrect answers, +0 for blanks

    Parameters
    ----------
    exam_key: {list} array of strings
    student_ans: {list} array of strings, may include blanks

    Returns
    -------
    {int}: total score for exam, return 0 if negative score

    Example
    -------
    >>> score_exam(['d', 'b', 'd', 'd'], ['b', '', '', 'b'])
    0
    >>> score_exam(['d', 'd', 'c', 'a'], ['b', '', 'c', 'a'])
    7
    >>> score_exam(['c', 'd', 'a', 'c'], ['c', 'b', 'a', 'b'])
    6
    """

    score = 0 # initial score
    for i in range(len(exam_key)): # iterate through the length of key
        if student_ans[i] == "": # first check if answer is blank
            continue
        elif exam_key[i] == student_ans[i]: # check answer is correct
            score += 4
        else: # check if answer is incorrect
            score -= 1
    return max(0, score) # return maximum, diregard negative value
