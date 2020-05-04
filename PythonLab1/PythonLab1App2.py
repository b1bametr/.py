#Написать скрипт, который выводит на экран «True», если элементы
#программно задаваемого списка представляют собой возрастающую
#последовательность, иначе – «False».


from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(-10, 10))
val=0
print(numbers)
try:

    if numbers[0]<numbers[1]:
       print("True")
    else:
        print("False")
except:
    print("Опаньки, что то пошло не так...")
