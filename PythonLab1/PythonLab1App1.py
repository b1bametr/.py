#Напишите скрипт, который преобразует введенное с клавиатуры
#вещественное число в денежный формат. Например, число 12,5 должно
#быть преобразовано к виду «12 руб. 50 коп.». В случае ввода
#отрицательного числа выдайте сообщение «Некорректный формат!»
#путем обработки исключения в коде.


num = float(input("Введите сумму: ")) 
try:
    if num >= 0:
        print(int(num), " руб.", round((num - int(num)) * 100), " коп.")  # целая часть числа + копейки

    elif num < 0:
        print("Некорректный формат!")
except:
  print("Опаньки, что то пошло не так...")