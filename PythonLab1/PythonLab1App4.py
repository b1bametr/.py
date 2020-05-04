#Напишите скрипт, который разделяет введенный с клавиатуры текст на
#слова и выводит сначала те слова, длина которых превосходит 7
#символов, затем слова размером от 4 до 7 символов, затем – все
#остальные.



text = input("Введите текст: ")
word=""
Fasle7=""
Fasle4=""
Fasle0=""
i=0
while i<len(text):
    if text[i].isalpha() == True:
        word = word+text[i]
    else:
        if len(word)>7:
            Fasle7=Fasle7+", "+word
        elif len(word)>=4 and len(word)<=7:
            Fasle4=Fasle4+", "+word           
        elif len(word)>0 and  len(word)<4:
            Fasle0=Fasle0+", "+word
        word = ""        
    i+=1
    
print (Fasle7[2:])
print (Fasle4[2:])
print (Fasle0[2:])