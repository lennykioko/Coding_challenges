# O(n + m) time | O(c) space - where n is the number of characters, m is
# the length of the document, and c is the number of unique characters in the characters string


def generateDocument(characters, document):
    """
    Best solution
    O(n) Time
    O(n) Space

    More accurate description
    O(n + m) Time
    O(c) Space
    """
    char_count = {}
    if document == '':
        return True
    for char in characters:
        char_count[char] = char_count.get(char, 0) + 1

    for letter in document:
        if char_count.get(letter):
            char_count[letter] -= 1
        else:
            return False
    return True


def generateDocument2(characters, document):
    """
    O(n + m) Time
    O(c) Space
    """
    charCount = {}

    for char in characters:
        if char not in charCount:
            charCount[char] = 0

        charCount[char] += 1

    for char in document:
        if char not in charCount or charCount[char] == 0:
            return False

        charCount[char] -= 1

    return True
