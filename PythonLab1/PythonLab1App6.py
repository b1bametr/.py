text="Город Донецк, река Кальмиус"
fin_characters=""
for word In text:
    if (fin_characters.find(word) is -1):
        fin_characters+=word+", "
else:
    fin_characters=(fin_characters[0:(len(fin_characters)-2)])
print(fin_characters)