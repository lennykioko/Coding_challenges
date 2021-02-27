def twoNumberSum(array, targetSum):
    """
    O(n2) Time
    O(1) Space
    """
    for i in range(0, len(array)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


def twoNumberSum2(array, targetSum):
    """
    O(n) Time
    O(n) Space
    """
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


array = [3, 5, -4, 8, 11, 1, 6, -1]
targetSum = 10
print(twoNumberSum(array, targetSum))
