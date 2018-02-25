def check_nums(num1, num2):
    if num2 > num1:
        return True
    elif num1 == num2:
        return "-1"
    else:
        return False

print(check_nums(20, 10))
print(check_nums(10, 10))
print(check_nums(10, 20))
