def recursive_binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


numbers = [num for num in range(1, 100)]

result = recursive_binary_search(numbers, 95)
verify(result)

result = recursive_binary_search(numbers, 250)
verify(result)
