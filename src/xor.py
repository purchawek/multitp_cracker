"""
module containing helper functions for
various xor operations
"""


def xor_two(lhs, rhs):
    """
    Function takes both parameters and returns as a result
    a string in which every element at position 'i' is a xor
    of i-th element of the first and the second.
    The result length equals length of shortest of the arguments.
    Args:
        lhs (str): first ciphertext to be xored
        rhs (str): second ciphertext to be xored
    Returns:
        str: xored result as described
    """
    length = min(len(lhs), len(rhs))
    res = ""
    for i in range(0, length):
        res += chr(ord(lhs[i]) ^ ord(rhs[i]))

    return res
