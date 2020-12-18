# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-12-09

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def simple_encrypt(text):
    """
    You need to encrypt each word in the message using following rules:
    The first letter needs to be converted to its ASCII code.
    The second letter needs to be switched with the last letter
    No special characters.

    Parameters
    ----------
    text: {str} message containing space separate words

    Returns
    -------
    {str}: encrypted message, after applying rules

    Example
    -------
    >>> simple_encrypt("A wise old owl lived in an oak")
    '65 119esi 111dl 111lw 108dvei 105n 97n 111ka'
    >>> simple_encrypt("Thank you Piotr for all your help")
    '84kanh 121uo 80roti 102ro 97ll 121ruo 104ple'
    >>> simple_encrypt("G nQvUXO NEgluNokOMLXHirbySa FNCG lQOCoLytHOmLUHuqQjm oPZfpGzhMlYjmlNohD qFGoexyaltGjZRPfh QCBMrRKW BpHBWCbegCcSzIfhRLHY uXnnjWKVdQPkK yQjHz FOqLlmsQz wPSwWk aUMMvfLVYPLQ diYUGRBtc AFBHvZu dKgISbaVvUd JCFCt JQNdNH SCDxXu qfnJgodQwFlmFde XZgIy lSlegCHlSbEx ZwgplqIitDLDodoSNwyj syvYoWnciqzyZQXjI svORw dqppjNPas BUcceyVwOoOzknNJB YPtrOrzTRuSXpNPY Pb hetWbLUOuaASn")
    '71 110OvUXQ 78agluNokOMLXHirbySE 70GCN 108mOCoLytHOmLUHuqQjQ 111DZfpGzhMlYjmlNohP 113hGoexyaltGjZRPfF 81WBMrRKC 66YHBWCbegCcSzIfhRLHp 117KnnjWKVdQPkX 121zjHQ 70zqLlmsQO 119kSwWP 97QMMvfLVYPLU 100cYUGRBti 65uBHvZF 100dgISbaVvUK 74tFCC 74HNdNQ 83uDxXC 113enJgodQwFlmFdf 88ygIZ 108xlegCHlSbES 90jgplqIitDLDodoSNwyw 115IvYoWnciqzyZQXjy 115wORv 100sppjNPaq 66BcceyVwOoOzknNJU 89YtrOrzTRuSXpNPP 80b 104ntWbLUOuaASe'
    """

    result = []
    for word in text.split():
        word = list(word) # turn word into a list
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        if len(word) > 2: # switch 2nd and last letters
            word[1], word[-1] = word[-1], word[1]
        result.append(''.join(word)) # add to results
    return ' '.join(result)
