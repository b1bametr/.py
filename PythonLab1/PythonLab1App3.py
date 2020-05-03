deb = input("Введите номер карты: ")
if len(deb) == 16:
   print(deb[0:4]+" **** **** "+deb[12:16])
else:
   print ("Некорректные данные!")