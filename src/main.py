"""
Main module showing menu and stuff
"""
import sys
from utils import utils
from xorcracker import XorCracker
from ciphertexts import Ciphertexts
from interactive import interactive

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
xor            - use xor attack on loaded ciphertexts
interactive    - enter interactive mode
        """
    )


def _handle_load(ciphertexts, cmd):
    if len(cmd) < 2:
        print("\"load\" requires filename")
        return
    fname = cmd[1]
    try:
        loaded_cnt = ciphertexts.load(fname)
        if loaded_cnt:
            print("Loaded {} ciphertexts".format(loaded_cnt))
        else:
            print("Couldn't load any ciphertexts. Check the format.")
    except FileNotFoundError:
        print("File {} does not exist".format(fname), file=sys.stderr)


@utils.for_loaded_only
def _handle_xor(ciphertexts):
    ciphertexts.key = XorCracker(ciphertexts).crack()
    utils.show_deciphered(ciphertexts)


def _handle_user_input(ciphertexts, cmd):
    if not cmd:
        return True
    if cmd[0] == 'exit':
        return False

    if cmd[0] == 'help':
        _show_help()
    elif cmd[0] == 'load':
        _handle_load(ciphertexts, cmd)
    elif cmd[0] == 'xor':
        _handle_xor(ciphertexts)
    elif cmd[0] == 'interactive':
        interactive.run_interactive(ciphertexts)
    else:
        print("This command is not valid. Type \"help\" to get help.")

    return True


def _main():
    ciphertexts = Ciphertexts()
    _say_hello()
    while _handle_user_input(ciphertexts, input().strip().split()):
        pass

if __name__ == "__main__":
    _main()
