def interpret(command):
    """
    O(n) Time
    O(n) Space
    """
    res = []
    for i in range(len(command)):
        if command[i] == "G":
            res.append(command[i])
        if command[i] == "(" and command[i + 1] == ")":
            res.append('o')
        if command[i] == "(" and command[i + 1] == "a" and command[i + 2] == "l" and command[i + 3] == ")":
            res.append("al")
    return "".join(res)
