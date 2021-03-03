def quick_sort(values):
    """
    Runtime of O(n2) in th worst-case scenario
    Runtime of O(n log n) in th best-case scenario

    More used in the real world compared to merge sort since
    its repeated operation is faster than merge sort's repeated
    operation
    """
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


numbers = [4, 6, 3, 2, 9, 7, 3, 5]
print(quick_sort(numbers))
