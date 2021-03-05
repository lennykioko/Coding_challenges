def findThreeLargestNumbers(array):
    """
    O(n) Time
    O(1) Space
    """
    big_three = [None, None, None]
    for num in array:
        update_results(big_three, num)
    return big_three


def update_results(big_three, num):
    if big_three[2] is None or num > big_three[2]:
        shift_and_update(big_three, num, 2)
    elif big_three[1] is None or num > big_three[1]:
        shift_and_update(big_three, num, 1)
    elif big_three[0] is None or num > big_three[0]:
        shift_and_update(big_three, num, 0)


def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:  # runs first becos we start from 0 counting upwards
            array[i] = array[i + 1]


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))
