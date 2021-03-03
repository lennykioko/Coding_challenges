def longestPalindrome(self, s: str) -> int:
    """
    O(n) Time
    O(n) Space
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    count = 0
    odd_present = False

    for char in char_count:
        if char_count[char] % 2 == 0:
            count += char_count[char]
        else:
            count += char_count[char] - 1
            odd_present = True

    if odd_present:
        count += 1

    return count
