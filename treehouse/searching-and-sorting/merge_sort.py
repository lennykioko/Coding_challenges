def merge_sort(values):
    """
    Rutime of O(n log n)
    """
    if len(values) <= 1:
        return values
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    sorted_values = []

    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1

        # handle lists of diff lengths
        # just append the rest of remaining list
        sorted_values += left_values[left_index:]
        sorted_values += right_values[right_index:]
        return sorted_values


numbers = [4, 6, 3, 2, 9, 7, 3, 5]
print(merge_sort(numbers))