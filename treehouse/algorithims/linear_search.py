def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


numbers = [num for num in range(1, 100)]

result = linear_search(numbers, 95)
verify(result)

result = linear_search(numbers, 250)
verify(result)
