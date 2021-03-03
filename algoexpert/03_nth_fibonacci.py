def getNthFib(n):
    """
    Recursive solution
    Worst solution
    O(2n) Time
    O(n) Space (recursion's call stack)
    """
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


def getNthFib2(n, memoize={1: 0, 2: 1}):
    """
    Using a cache to optimize recursive call
    O(n) Time
    O(n) Space
    """
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(memoize[n - 1], memoize) + getNthFib2(memoize[n - 2])
    return memoize[n]


def getNthFib3(n):
    """
    Best solution
    O(n) Time
    O(1) Space
    """
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[1] + last_two[0]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    # handle the edge case where n = 1
    return last_two[1] if n > 1 else last_two[0]
