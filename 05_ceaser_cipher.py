def caesarCipherEncryptor(string, key):
    """
    O(n) Time
    O(n) Space
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    coded_msg = []
    key %= 26

    for letter in string:
        # careful with .index operation, can fix by implementing a dict instead
        new_letter_key = alphabet.index(letter) + key
        new_letter_key %= 26
        coded_msg.append(alphabet[new_letter_key])

    return "".join(coded_msg)


################################################

def caesarCipherEncryptor4(string, key):
    """
    O(n) Time
    O(n) Space
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    by_string = {}
    by_index = {}
    for index, value in enumerate(alphabet):
        by_index[index] = value
        by_string[value] = index

    coded_msg = []
    key %= 26

    for letter in string:
        new_letter_key = by_string[letter] + key
        new_letter_key %= 26
        coded_msg.append(by_index[new_letter_key])

    return "".join(coded_msg)


################################################


def getCodedLetter(letter, key):
    """
    ord('a') = 97
    ord('z') = 122
    chr(97) = 'a'
    chr(122) = 'z'
    """
    new_code = ord(letter) + key
    return chr(new_code) if new_code <= 122 else chr(96 + (new_code % 122))


def caesarCipherEncryptor2(string, key):
    """
    Best solution
    O(n) Time
    O(n) Space
    """
    coded_msg = []
    key %= 26

    for letter in string:
        coded_msg.append(getCodedLetter(letter, key))
    return "".join(coded_msg)


################################################

def getCodedLetter2(letter, key, alphabet):
    new_code = alphabet.index(letter) + key
    return alphabet[new_code % 26]


def caesarCipherEncryptor3(string, key):
    """
    O(n) Time
    O(n) Space
    """
    coded_msg = []
    key %= 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in string:
        coded_msg.append(getCodedLetter2(letter, key, alphabet))
    return "".join(coded_msg)


print(caesarCipherEncryptor4('abc', 2))
print(caesarCipherEncryptor4('xyz', 2))
print(caesarCipherEncryptor4('abc', 28))
