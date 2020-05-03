from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(-10, 10))
val=0
for i in range(20): 
    val=val+numbers[i]
print(numbers)
if val>=0:
   print("True")
else:
    print("False")
