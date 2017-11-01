"""
Module that tests the package functionality as a whole
"""
import unittest

from src.xorcracker import XorCracker
from src.ciphertexts import Ciphertexts

class TestBasic(unittest.TestCase):
    """
    Test the whole mechanism of reading input -> parsing -> xor cracking
        -> parsing to output
    """
    def test_simple(self):
        """
        Test the most basic example
        """
        ciphertexts = Ciphertexts()
        ciphertexts.load("tests/crypto01")
        key = XorCracker(ciphertexts).crack()
        decrypted = ciphertexts.tostring(ciphertexts.size()-1, key)
        self.assertEqual(decrypted,
                         '#Z#na Hollywood": "#miem pisac i czytac, ale powoli#"')
