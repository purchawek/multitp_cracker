"""
Module holding various helper functions
"""

def get_deciphered(ciphertexts):
    """
    Function that takes the ciphertexts and parses them
    to a visible deciphered format
    """
    deciphered = []
    for i, _ in enumerate(ciphertexts.ctexts):
        deciphered.append(ciphertexts.tostring(i))
    return deciphered


def show_deciphered(ciphertexts):
    for i, plaintxt in enumerate(get_deciphered(ciphertexts)):
        print(i, plaintxt, end='\n\n')

def for_loaded_only(func):
    """
    Decorator for asserting that the passed function is
    run only if the ciphertexts are loaded
    """
    def _inner(ciphertexts, *args, **kwargs):
        if not ciphertexts.loaded():
            print("You didn't load any ciphertexts. Try \"load\"")
            return
        return func(ciphertexts, *args, **kwargs)
    return _inner
