from random import randint
import math

array = [randint(0, 100) for i in range(randint(1, 10000))]
print('В начале работы скрипта элементов: ', len(array))
Pow = math.ceil(math.log2(len(array))) 
[array.append(0) for i in range(len(array), 2 ** Pow)]

print('Стало элементов после скрипта: ', len(array), '\nСтепень: ', Pow)
