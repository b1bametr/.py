#Напишите собственную версию генератора enumerate под названием
#extra_enumerate. Пример вызова:
#В переменной cum хранится накопленная сумма на момент текущей
#итерации, в переменной frac – доля накопленной суммы от общей
#суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
#вывод будет таким:


def extra_enumerate(x):
    cum = 0
    fraction = 0
    for step in x:
        fraction += step
    for i in range(len(x)):
        elem = x[i]
        cum += x[i]
        frac = cum / fraction
        yield i, elem, cum, round(frac, 1)


x = [i for i in range(15)]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
