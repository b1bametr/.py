password = input('Введите пароль')
pass_safety = 0
flag = True

if len(password) > 16:
    pass_safety += 2
elif len(password) > 8:
    pass_safety += 1
else:
    pass_safety -= 1


if password.islower():
    pass_safety -= 5
    flag = False
if password.isdigit():
    pass_safety -= 5
    flag = False
if password.isupper():
    pass_safety -= 5
    flag = False


for i in range(len(password)):
    if password[i].isdigit() and flag is not False:
        pass_safety += 1
    if password[i].isupper() and flag is not False:
        pass_safety += 1


if pass_safety > 10:
    print('Хороший пароль! (' + str(pass_safety) + ')')
elif 5 <= pass_safety <= 10:
    print('Уровень защиты с данным паролем плох.(' + str(pass_safety) + ')')
elif pass_safety < 5:
    print('Вы ввели неподходящий пароль!(' + str(pass_safety) + ')')

