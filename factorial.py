def first_factorial(num): 

  for i in range(1, num):
      num = num * i
   
  print(num)

first_factorial(4)
print(4*3*2*1)
first_factorial(8)
print(8*7*6*5*4*3*2*1)
