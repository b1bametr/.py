real = input("Введите сумму: ")

if float(real) >= 0:
	print(real[0:real.find(".")] + " руб." + real[real.find(".")+1:len(real)] + " коп.")
else:
	print ("Некорректный формат!")