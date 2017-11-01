
class CiphersParser:

    @staticmethod
    def parse_binary(line):
        result = ""
        for word in line.split():
            result += chr(int(word, 2))
        return result

    @staticmethod
    def parse_hexstring(line):
        pass


class Ciphertexts:
    def __init__(self):
        self._ctexts = []

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
            self._ctexts += loaded
            return len(loaded)
        return 0

    def loaded(self):
        return len(self._ctexts) != 0