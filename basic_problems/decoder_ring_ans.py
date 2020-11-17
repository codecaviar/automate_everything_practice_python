# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-26

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

def decoder_ring(cipher_text):
    """
    Return the plain alphabet text from the cipher alphabet, where
    encryption is completed by replacing space with keyword "XYZ"

    Parameters
    ----------
    cipher_text: {str} single, non-empty string, consisting only of
        uppercase English letters, length does not exceed 200 characters

    Returns
    -------
    {str}: words of the initial plain text used to make a cipher text,
        separate the words with a space

    Example
    -------
    >>> decoder_ring("XYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZWHATXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZXYZ")
    'WHAT'
    >>> decoder_ring("WXYZHXYZEXYZN")
    'W H E N'
    >>> decoder_ring("HOWXYZXYZXYZWHY")
    'HOW WHY'
    """

    # Optional: use try...except block to handle error conditions

    # Use the replace method to find keyword
    # Use the split method to separate words at the space character
    decrypt_text = cipher_text.replace("XYZ", " ").split()

    replace_space = " ".join(decrypt_text) # Rejoin the list of words

    return replace_space
