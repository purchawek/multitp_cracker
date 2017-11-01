"""
Module containing a class able to perform a xor attack
"""


class XorCracker:
    """
    Main class responsible for performing a xor crack.
    It allows to attack by specifying a char or by using auto
    """
    def __init__(self, ciphertexts):
        dict_visible = ('abcdefghijklmnopqrstuvwxyz' +
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
                        ' ?:,."#')
        self.dict_visible = [ord(x) for x in dict_visible]
        self._ciphertexts = ciphertexts.ctexts
        self._key = ciphertexts.key
        self._max_len = max([len(x) for x in self._ciphertexts])
        self._to_decrypt = list(range(self._max_len))

    def getkeychar(self, cindex, ccol, char):
        """
        Get value that xored with cindex[ccol] will give 'char'
        in the plaintext. The result is possible value
        for the key in this column.

        Returns:
            int: possible value for the key in the given column
        """
        return self._ciphertexts[cindex][ccol] ^ ord(char)

    def setkeychar(self, col, char):
        self._key[col] = char

    def _addifsolved(self, potentialkeychar, col):
        for ciph in self._ciphertexts:
            if col >= len(ciph):
                continue
            if ciph[col] ^ potentialkeychar not in self.dict_visible:
                return
        self._key[col] = potentialkeychar
        try:
            self._to_decrypt.remove(col)
        except ValueError:
            pass

    def getkey(self):
        """
        Returns:
            key (dict(int, int)) - dict key is column number
                and the value is presumable value of the key
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
                    self._addifsolved(self.getkeychar(i, col, ' '), col)
        return self._key
