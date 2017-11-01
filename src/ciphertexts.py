
class CiphersParser:
    """
    Simple class for parsing the ciphertexts into format required by
    the library
    """
    @staticmethod
    def parse_binary(line):
        result = []
        for word in line.split():
            result.append(int(word, 2))
        return result

    @staticmethod
    def parse_hexstring(line):
        pass


class Ciphertexts:
    """
    Class packing all the data required to work with ciphertexts together
    """
    def __init__(self):
        self.ctexts = []
        self.key = {}

    def load(self, fname):
        """
        Function responsible for loading ciphertexts from file.
        Args:
            fname (str): file to look for ciphertexts in
        """
        with open(fname) as c_file:
            loaded = [
                CiphersParser.parse_binary(l.strip()) for l in c_file
                if len(l.strip()) > 0
            ]
            self.ctexts += loaded
            return len(loaded)
        return 0

    def size(self):
        """
        Returns number o ciphertexts
        """
        return len(self.ctexts)

    def loaded(self):
        """
        Returns:
            bool: if there are any ciphertexts loaded
        """
        return self.size() != 0

    def tostring(self, index):
        """
        Function that converts single cryptogram
        to a plaintext with aqquired key.
        """
        if index < 0 or index >= len(self.ctexts):
            return None

        ctext = self.ctexts[index]
        result = [chr(ctext[i] ^ self.key[i])
                  if i in self.key
                  else '#'
                  for i in range(len(ctext))]
        return ''.join(result)
