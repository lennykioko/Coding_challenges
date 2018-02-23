def first_factorial(num): 

  for i in range(1, num):
      num = num * i
   
  print(num)

first_factorial(4)
print(4*3*2*1)
first_factorial(8)
print(8*7*6*5*4*3*2*1)

# better solution
def first_factorial_2(num):
    factorial = 1

    if num < 0:
        print("The factorial for this number does not exist")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, (num+1)):
            factorial *= i
        print("The factorial of {} is {}".format(num, factorial))

first_factorial_2(-1)
first_factorial_2(0)
first_factorial_2(4)
print(4*3*2*1)
first_factorial_2(8)
print(8*7*6*5*4*3*2*1)

# factorial using recursion
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
if num < 0:
    print("Negative numbers do not have a factorial")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of {} is {}".format(num, factorial(num)))
