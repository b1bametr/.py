#Напишите скрипт, который позволяет ввести с клавиатуры имя
#текстового файла, найти в нем с помощью регулярных выражений все
#подстроки определенного вида, в соответствии с вариантом.
#Например,
#для варианта № 1 скрипт должен вывести на экран следующее:
#Строка 3, позиция 10 : найдено '11-05-2014'
#Строка 12, позиция 2 : найдено '23-11-2014'
#Строка 12, позиция 17 : найдено '23-11-2014'
#Вариант 11. т.е. 1: найдите все даты – подстроки вида «11-05-2014»


import re

content = ''
path = input('Введите название вашего файла (без расширения) Подсказка: введите 1: ') +".txt"
try:
    file = open("" + path, 'r', encoding='UTF-8')
    content = file.read().replace('\n', ' ')
    file.close()
except FileNotFoundError as e:
    print('Опаньки, что то пошло не так...', e.args)

result = re.findall(r"\d\d\S\d\d\S\d\d\d\d", content)
with open('1.txt', 'rt', encoding='UTF-8') as file:
    z=0
    while z<len(result): 
        for index, line in enumerate(file,1):       
            if result[z] in line:
                print("Строка "+str(index)+" позиция "+str(line.find(result[z]))+" : найдено "+str(result[z]))
                z+=1