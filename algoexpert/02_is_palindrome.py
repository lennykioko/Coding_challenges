def isPalindrome4(string):
    """
    Best solution
    O(n) Time
    O(1) Space
    """
    leftIndex = 0
    rightIndex = len(string) - 1

    while leftIndex < rightIndex:
        if string[leftIndex] != string[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True


def isPalindrome(string):
    """
    O(n) Space
    O(n) Time
    """
    backwards = []
    arr = list(string)
    if len(arr) == 1:
        return True
    for i in range(len(arr) - 1, -1, -1):
        backwards.append(arr[i])
    return arr == backwards


def isPalindrome2(string):
    """
    O(n) Space
    O(n) Time
    """
    backwards = []
    if len(string) == 1:
        return True
    for i in range(len(string) - 1, -1, -1):
        backwards.append(string[i])
    return string == "".join(backwards)


def isPalindrome3(string):
    """
    O(n) Space
    O(n) Time
    """
    backwards = []
    for i in reversed(range(0, len(string))):
        backwards.append(string[i])
    return string == "".join(backwards)


def isPalindrome5(string, i=0):
    """
    O(n) Time
    O(1) Space (becoz the call stack takes on additional space)
    """
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome5(string, i + 1)


def isPalindrome6(string, i=0):
    """
    Recursive solution
    O(n) Time
    O(1) Space (becoz the call stack takes on additional space)
    """
    j = len(string) - 1 - i
    if i >= j:  # base condition
        return True
    if string[i] != string[j]:
        return False

    return isPalindrome5(string, i + 1)


text = "bob"
print(isPalindrome6(text))
