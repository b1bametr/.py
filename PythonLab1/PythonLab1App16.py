from random import shuffle
import itertools
import time
from time import strftime
from datetime import timedelta, datetime

format = "%d/%m/%Y, %H:%M"
start = datetime.strptime("14/09/2016, 22:45", format)
teams = [
    'ФК Шахтёр', 'Динамо Киев', 'Днепр', 'Севилья',
    'Реал-Сосьедад', 'Реал-Мадрид', 'Барселона', 'Атлетико',
    'МЮ', 'Арсенал', 'Ювентус', 'Тоттенхэм',
    'Интер', 'Ливерпуль', 'ЦСК', 'Зенит'
]
shuffle(teams)
teams = [teams[i*4: i*4+4] for i in range(0, 4)]
games = []
for t in teams:
    games.append([i for i in itertools.combinations(t, 2)])
for i in range(0, 6):
    print(start.strftime(format))
    print("Game: ", i + 1)
    print(games[0][i])
    print(games[1][i])
    print(games[2][i])
    print(games[3][i])
    start = start + timedelta(days=14)
print("Championship is over !!!")
print(start.strftime(format))