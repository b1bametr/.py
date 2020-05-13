
#Введите с клавиатуры текст. Программно найдите в нем и выведите
#отдельно все слова, которые начинаются с большого латинского
#символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
#«Petr93», «Johnny70», «Service2002». Используйте регулярные
#выражения.

#Пример текста:
#Biba12455 boba23 Bulbozavr22 Wiver3333 Zerrrrrrr

import re
import string

upper_letters = string.ascii_uppercase
pattern = re.compile(r'[A-Z]\S\D+\d{2,4}')
text = input('Введите текст: ')

result = re.findall(pattern, text)
print(result)

