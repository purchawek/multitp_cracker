"""
Main module showing menu and stuff
"""
import sys
from xorcracker import XorCracker
from ciphertexts import Ciphertexts

def _say_hello():
    print(
        """
Multi Time Pad Cracker
Tool intended to show that in stream ciphers it's super important
to never reuse the same key.

Type 'help' to get help.
        """
    )

def _show_help():
    print(
        """
load <fname>   - load ciphertexts from "fname" file
        """
    )


def _prepare_deciphered(ciphertexts, key):
    deciphered = []
    for c in ciphertexts:
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


def _handle_user_input(ciphertexts, cmd):
    if not cmd:
        return True

    if cmd[0] == 'help':
        _show_help()
    elif cmd[0] == 'load' and len(cmd) >= 2:
        try:
            loaded_cnt = ciphertexts.load(cmd[1])
            if loaded_cnt:
                print("Loaded {} ciphertexts".format(loaded_cnt))
            else:
                print("Couldn't load any ciphertexts. Check the format.")
        except FileNotFoundError:
            print("File {} does not exist".format(cmd[1]), file=sys.stderr)
    elif cmd[0] == 'xor':
        if not ciphertexts.loaded():
            print("You didn't load any ciphertexts. Try \"load\"")
            return True
        decrypted = _prepare_deciphered(ciphertexts._ctexts, XorCracker(ciphertexts).crack())
        for d in decrypted:
            print(''.join(d), end='\n\n')
    elif cmd[0] == 'exit':
        return False;

    return True


def _main():
    ciphertexts = Ciphertexts()
    _say_hello()
    while _handle_user_input(ciphertexts, input().strip().split()):
        pass

if __name__ == "__main__":
    _main()
