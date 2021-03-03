def merge_sort(mylist):
    """
    Sorts list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide it into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step

    Takes O(n log n) time
    """

    if len(mylist) <= 1:
        return mylist

    left_half, right_half = split(mylist)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(mylist):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) time
    """

    midpoint = len(mylist) // 2
    # splitting this way does not take contant time instead
    # instead it takes k where k is the size of the list
    # si with this implementation it is O(k log n)
    # like you did in binary/linear_search you can use iteraive solution
    # and avoid using this split function and remove the extra time complexity
    left = mylist[:midpoint]
    right = mylist[midpoint:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    sl = []  # sorted list
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sl.append(left[i])
            i += 1
        else:
            sl.append(right[j])
            j += 1

    # when lenth of two sublists are not equal
    while i < len(left):
        sl.append(left[i])
        i += 1

    while j < len(right):
        sl.append(right[j])
        j += 1

    return sl


def verify_soted(mylist):
    n = len(mylist)

    if n == 0 or n == 1:
        return True

    return mylist[0] < mylist[1] and verify_soted(mylist[1:])


def verify_soted_iterative(mylist):
    n = len(mylist)

    if n == 0 or n == 1:
        return True

    for i in range(0, len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            return False

    return True


al = [11, 6, 55, 77, 98, 43, 23, 13, 84]
sl = merge_sort(al)

print(verify_soted(al))
print(verify_soted(sl))

print(verify_soted_iterative(al))
print(verify_soted_iterative(sl))
