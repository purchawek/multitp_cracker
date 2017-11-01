import sys
import ctypes
import re
from ctypes import cdll

lib = cdll.LoadLibrary("bin/libfindclosest.so")
lib.find_closest.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.find_closest.restype = ctypes.c_char_p

SMALL = 'abcdefghijklmnopqrstuvwxyz'
BIG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS = SMALL + BIG

DICT_VISIBLE = ('abcdefghijklmnopqrstuvwxyz' +
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
                ' ?:,."#')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("fname missing")
        sys.exit()
    fname = sys.argv[1]

    def read_crypto(fname):
        cryptograms = []
        with open(fname) as cfile:
            for line in cfile:
                line = line.strip()
                if len(line) > 0:
                    cryptograms.append(parse_crypto(line))
        return cryptograms

    def parse_crypto(line):
        result = ""
        for word in line.split():
            result += chr(int(word, 2))
        return result

    def xor_two(lhs, rhs):
        length = min(len(lhs), len(rhs))
        res = ""
        for i in range(0, length):
            res += chr(ord(lhs[i]) ^ ord(rhs[i]))

        return res

    cryptograms = read_crypto(fname)

    max_len = max([len(x) for x in cryptograms])
    cryp_cnt = len(cryptograms)
    to_decrypt = [i for i in range(max_len)]

    def getkeychar(cindex, ccol, char):
        return chr(ord(cryptograms[cindex][ccol]) ^ ord(char))

    key = {}

    def addifsolved(potentialkeychar, col):
        for x in cryptograms:
            if col >= len(x):
                continue
            c = chr(ord(x[col]) ^ ord(potentialkeychar))
            if c not in DICT_VISIBLE:
                return
        key[col] = potentialkeychar
        try:
            to_decrypt.remove(col)
        except ValueError:
            pass

    def decryptchar(j, col):
        return chr(ord(cryptograms[j][col]) ^ ord(key[col]))

    for j in range(cryp_cnt - 1):
        to_decrypt_copy = [i for i in to_decrypt]
        for col in to_decrypt_copy:
            if col < len(cryptograms[j]):
                addifsolved(getkeychar(j, col, ' '), col)

    for j in range(cryp_cnt - 1):
        to_decrypt_copy = [i for i in to_decrypt]
        for col in to_decrypt_copy:
            if col >= len(cryptograms[j]):
                continue
            if col == 0:
                for c in BIG:
                    addifsolved(getkeychar(j, col, c), col)
            elif col - 1 in key:
                decipchar = decryptchar(j, col-1)
                if decipchar in LETTERS:
                    for c in SMALL:
                        addifsolved(getkeychar(j, col, c), col)
                else:
                    index = col-2
                    while (index > 0 and index-1 in key
                           and decryptchar(j, index-1) == ' '):
                        index -= 1

                    deciphar = decryptchar(j, index)
                    if deciphar not in LETTERS:
                        for c in BIG:
                            addifsolved(getkeychar(j, col, c), col)
                    else:
                        for c in LETTERS:
                            addifsolved(getkeychar(j, col, c), col)

    print("DECRYPTED: ", len(key))
    print()

    def prepare_deciphered():
        deciphered = []
        for c in cryptograms:
            deciphered.append([])
            last = deciphered[len(deciphered)-1]
            for x in c:
                last.append(x)

            for i in range(len(last)):
                if i in key:
                    last[i] = chr(ord(last[i]) ^ ord(key[i]))
                else:
                    last[i] = '#'
        return deciphered

    deciphered = prepare_deciphered()

    lib.load(b"tests/odm2.txt")
    result = ctypes.create_string_buffer(128)

    def lower(c):
        if c >= 'A' and c <= 'Z':
            return chr(ord(c) + 32)
        return c

    def addifsolved(potentialkeychar, col):
        for x in cryptograms:
            if col >= len(x):
                continue
            c = chr(ord(x[col]) ^ ord(potentialkeychar))
            if c not in DICT_VISIBLE:
                return False
        key[col] = potentialkeychar
        return True

    def try_dictionary(col, prev, proposal):
        if prev == proposal:
            return
        for i in range(len(prev)):
            if lower(prev[i]) != lower(proposal[i]):
                if addifsolved(
                        getkeychar(j, col+i, proposal[i]), col+i):
                    print(bcolors.OKGREEN, end="")
                else:
                    print(bcolors.FAIL, end="")
                print(prev, proposal, bcolors.ENDC)

    for j in range(len(cryptograms)):
        current = deciphered[j]
        dectext = ''.join(current)
        for word in re.split("[,\.\?\": ]", dectext):
            if '#' not in word and len(word) > 3:
                if word[len(word)-1] in ',.?:':
                    word = word[:-1]
                try:
                    try_dictionary(
                        dectext.find(word),
                        word,
                        lib.find_closest(
                            bytes(word, 'ascii'), result).decode('ascii'))
                except UnicodeDecodeError:
                    pass

    for d in prepare_deciphered():
        print(''.join(d))
        print()
