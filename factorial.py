def first_factorial(num): 

  for i in range(1, num):
      num = num * i
   
  print(num)

first_factorial(4)
print(4*3*2*1)
first_factorial(8)
print(8*7*6*5*4*3*2*1)

# better solution
def second_factorial(num):
    factorial = 1

    if num < 0:
        print("The factorial for this number does not exist")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, (num+1)):
            factorial *= i
        print("The factorial of {} is {}".format(num, factorial))

second_factorial(-1)
second_factorial(0)
second_factorial(4)
print(4*3*2*1)
second_factorial(8)
print(8*7*6*5*4*3*2*1)
