def smallerNumbersThanCurrent(nums):
    """
    O(n log n) Time
    O(n) Space
    """
    s_nums = sorted(nums)
    results = {}
    for index, value in enumerate(s_nums):
        if results.get(value) is None:
            results[value] = index

    output = []
    for num in nums:
        output.append(results[num])

    return output
