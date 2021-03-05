def bubbleSort(array):
    """
    Best solution
    O(n2) Time
    O(1) Space
    """
    end = len(array)
    complete = False

    while not complete:
        swap = 0
        for i in range(0, end - 1):
            if array[i] > array[i + 1]:
                # c = a, a = b, b = c
                array[i], array[i + 1] = array[i + 1], array[i]
                swap += 1
        if swap == 0:
            complete = True
        end -= 1  # optimization for last item being sorted
    return array


def bubbleSort2(array):
    """
    O(n2) Time
    O(1) Space
    """
    end = len(array)
    complete = False

    while not complete:
        swap = 0
        for i in range(0, end):
            if i < end - 1:
                if array[i] > array[i + 1]:
                    # c = a, a = b, b = c
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swap += 1
        if swap == 0:
            complete = True
        end -= 1  # optimization for last item being sorted
    return array


def bubbleSort3(array):
    """
    O(n2) Time
    O(1) Space
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def bubbleSort4(array):
    """
    O(n2) Time
    O(1) Space
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
    return array


def swap2(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
