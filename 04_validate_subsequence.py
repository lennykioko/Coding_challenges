def isValidSubsequence2(array, sequence):
    """
    Best solution
    O(n) Time
    O(1) Space
    """
    index = 0
    for num in array:
        if index == len(sequence):
            # save time and exit if we have exhausted items in sequence
            break
        if index < len(sequence):
            if num == sequence[index]:
                index += 1

    return index == len(sequence)


def isValidSubsequence(array, sequence):
    """
    O(n) Time
    O(1) Space
    """
    index = 0
    for num in array:
        # in an array of 5 items, indexes are 0, 1, 2, 3, 4
        if index <= len(sequence) - 1:
            if num == sequence[index]:
                index += 1

    return index > len(sequence) - 1


def isValidSubsequence3(array, sequence):
    """
    O(n) Time
    O(1) Space
    """
    arr_index = 0
    seq_index = 0
    while arr_index < len(array) and seq_index < len(sequence):
        if array[arr_index] == sequence[seq_index]:
            seq_index += 1

        # we always increment array index but only increment seq index when we have a match
        arr_index += 1

    return seq_index == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence3(array, sequence))
