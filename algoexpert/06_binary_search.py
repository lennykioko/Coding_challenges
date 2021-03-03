def binarySearch(array, target):
    """
    Best solution
    O(log n) Time
    O(1) Space
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = (left + right) // 2
        if target == array[midpoint]:
            return midpoint
        elif target < array[midpoint]:
            right = midpoint - 1
        elif target > array[midpoint]:
            left = midpoint + 1

    return -1



def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    """
    O(log n) Time
    O(1) Space
    """
    while left <= right:
        midpoint = (left + right) // 2
        if target == array[midpoint]:
            return midpoint
        elif target < array[midpoint]:
            right = midpoint - 1
        elif target > array[midpoint]:
            left = midpoint + 1

    return -1


#################################

def binarySearch2(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper2(array, target, left, right):
    """
    O(log n) Time
    O(log n) Space  - Due to additional frames on  the call-stack becoz of recursion
    """
    if left > right:
        return -1
    midpoint = (left + right) // 2
    if target == array[midpoint]:
        return midpoint
    elif target > array[midpoint]:
        left = midpoint + 1
        return binarySearchHelper2(array, target, left, right)
    # being very explicit about the condition and not using else
    elif target < array[midpoint]:
        right = midpoint - 1
        return binarySearchHelper2(array, target, left, right)
