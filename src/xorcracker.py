"""
Module containing a class able to perform a xor attack
"""


class XorCracker:
    """
    Main class responsible for performing a xor crack.
    It allows to attack by specifying a char or by using auto
    """
    def __init__(self, ciphertexts):
        self.dict_visible = ('abcdefghijklmnopqrstuvwxyz' +
                             'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
                             ' ?:,."#')
        self._ciphertexts = ciphertexts._ctexts
        self._key = {}
        self._max_len = max([len(x) for x in self._ciphertexts])
        self._to_decrypt = list(range(self._max_len))

    def _getkeychar(self, cindex, ccol, char):
        return chr(ord(self._ciphertexts[cindex][ccol]) ^ ord(char))

    def _addifsolved(self, potentialkeychar, col):
        for x in self._ciphertexts:
            if col >= len(x):
                continue
            c = chr(ord(x[col]) ^ ord(potentialkeychar))
            if c not in self.dict_visible:
                return
        self._key[col] = potentialkeychar
        try:
            self._to_decrypt.remove(col)
        except ValueError:
            pass

    def getkey(self):
        """
        Return:
        """
        return self._key

    def crack(self):
        """
        Function that perform classical xor-attack on the
        given ciphertexts
        """
        to_decrypt_copy = list(range(self._max_len))

        for i in range(len(self._ciphertexts)):
            for col in to_decrypt_copy:
                if col < len(self._ciphertexts[i]):
                    self._addifsolved(self._getkeychar(i, col, ' '), col)
        return self._key
