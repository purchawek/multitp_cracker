"""
Container for strings used in the module
"""

STRINGS = {
    'header': """
Welcome to the Interactive Mode!
Type "help" to get help.
    """,
    'help': """
Interactive Mode
Press <Enter> to show all the ciphertexts in the currently decrypted form.

This mode allows you to try deciphering the texts by hand (which is often
very efficient). You can do it by specifying three variables:
<ciphertext_id>
<character_to_replace>
<new_character>

The program will then take the ciphertext of a given id, find FIRST occurence of the
character you typed and replace it with the new one. It will also do proper change
in all the other ciphertexts so you can see if your proposition doesn't make any
mess.

You can also search by substring. When you do that, only the first character of
the first occurence of the substring is changed to the new_character
    """,
    'empty_key_warning': """
WARNING: your key is almost empty. You can still work on it,
but it's gonna be hard. Maybe try \"xor\" before?
    """,
    'usage': """
USAGE:
<ciphertext_id> <character_to_replace> <new_character>
    """,
    'invalid_col': """
    Column doesn't fit
    """
}
