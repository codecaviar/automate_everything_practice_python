# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-10-26

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

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

    pass # null operation, placeholder when a statement is required
