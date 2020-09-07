from string import ascii_uppercase


class CaesarCipher:
    def __init__(self):
        self.SCALE = 65

    def encrypt(self, string, key):
        """
        encrypt a message based on a given key
        :param string: string to be encrypted
        :param key: encryption key
        :return: encrypted message
        """
        result = ""
        string = string.upper()
        key = ord(key.upper()) - self.SCALE
        for letter in string:
            if letter in ascii_uppercase:
                letter = ord(letter)
                result += chr(((letter - self.SCALE + key) % 26) + self.SCALE)
            else:
                result += letter
        return result

    def decrypt(self, string, key):
        """
        decrypt a message based on a given key
        :param string: string to be decrypted
        :param key: decryption key
        :return: decrypted message
        """
        result = ""
        string = string.upper()
        key = ord(key.upper()) - self.SCALE
        for letter in string:
            if letter in ascii_uppercase:
                letter = ord(letter)
                result += chr(((letter - self.SCALE - key) % 26) + self.SCALE)
            else:
                result += letter
        return result

    def get_key(self, string, encrypted_string):
        """
        get the encryption/decryption key
        :param string: string message
        :param encrypted_string: corresponding encrypted message
        :return: encryption key
        """
        key = ''
        for i in ascii_uppercase:
            if self.encrypt(string, i) == encrypted_string:
                key += i
        return key


# Instantiate CaesarCiper()
cipher = CaesarCipher()

# Test Case for Encryption
print(cipher.encrypt('DARRYL SEE WEI SHEN', 'X'))

# Test Case for Decryption
print(cipher.decrypt('AXOOVI PBB TBF PEBK', 'X'))

# Test Case for Get Key
print(cipher.get_key('DARRYL SEE WEI SHEN', 'AXOOVI PBB TBF PEBK'))
