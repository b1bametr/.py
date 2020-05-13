#Напишите скрипт, который читает текстовый файл и выводит символы
#в порядке убывания частоты встречаемости в тексте. Регистр символа
#не имеет значения. Программа должна учитывать только буквенные
#символы (символы пунктуации, цифры и служебные символы слудет
#игнорировать). Проверьте работу скрипта на нескольких файлах с
#текстом на английском и русском языках, сравните результаты с
#таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies


try:
    txt = open('sample1.txt', 'r').read()  # читаем  // 2 тестовых файла sample1.txt и sample2.txt
except IOError as err:
    print("Опаньки, что то пошло не так...")
dic = {letter: txt.count(letter) for letter in txt if letter.isalpha()} # создаем
for key in sorted(dic.keys(), key=dic.get, reverse=True):print(key, ': ', dic[key]) # сортируем/выводим
    
