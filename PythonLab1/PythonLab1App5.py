text="Город Донецк, река Кальмиус"           
text=text.split() 
res=[]
for word in text:   
    if(word.istitle()):
        res.append(word.upper())
    else:
        res.append(word)
newtext=(" ".join(res))
print(newtext)