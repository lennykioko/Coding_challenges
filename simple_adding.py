def simple_adding(num):
    sum = 0
    
    for i in range(1, (num+1)):
        sum += i
        
    return sum

print(simple_adding(4))
print(4+3+2+1)
print(simple_adding(8))
print(8+7+6+5+4+3+2+1)

# clever solution
def simple_adding_2(num): 
  return (num*(num+1))//2
    
print(simple_adding_2(4))
print(simple_adding_2(8))