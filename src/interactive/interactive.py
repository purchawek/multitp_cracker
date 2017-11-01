"""
Module implementing the interactive mode.
"""
from utils import utils
from interactive.strings import STRINGS
from xorcracker import XorCracker


def _check_user_guess(ciphertexts, cid, patt, repl):
    cracker = XorCracker(ciphertexts)
    try:
        patt_index = ciphertexts.tostring(cid).find(patt)
        cracker.setkeychar(patt_index,
                           cracker.getkeychar(cid, patt_index, repl))
        ciphertexts.key = cracker.getkey()
        utils.show_deciphered(ciphertexts)
    except IndexError:
        print(STRINGS['invalid_col'])


def _handle_input(ciphertexts, cmd):
    if not cmd:
        utils.show_deciphered(ciphertexts)
    elif cmd[0] == 'exit':
        return False
    elif cmd[0] == 'help':
        print(STRINGS['help'])
    else:
        try:
            cid, patt, repl = int(cmd[0]), cmd[1], cmd[2]
            _check_user_guess(ciphertexts, cid, patt, repl)
        except (IndexError, ValueError):
            print(STRINGS['usage'])


    return True


def _show_interactive_header():
    print(STRINGS['header'])


@utils.for_loaded_only
def run_interactive(ciphertexts):
    """
    Main function of the interactive mode
    """
    print(STRINGS['help'])

    key = ciphertexts.key
    if not key:
        print(STRINGS['empty_key_warning'])
    while _handle_input(ciphertexts, input().strip().split()):
        pass
