def binary_search(mylist, target):
    first = 0
    last = len(mylist) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if mylist[midpoint] == target:
            return midpoint
        elif mylist[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None
