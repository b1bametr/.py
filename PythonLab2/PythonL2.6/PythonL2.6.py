#Напишите скрипт reorganize.py, который в директории --source создает
#две директории: Archive и Small. В первую директорию помещаются
#файлы с датой изменения, отличающейся от текущей даты на
#количество дней более параметра --days (т.е. относительно старые
#файлы). Во вторую – все файлы размером меньше параметра --size байт.
#Каждая директория должна создаваться только в случае, если найден
#хотя бы один файл, который должен быть в нее помещен. Пример
#вызова:
#reorganize6 --source "E:/Python/Laba2/Music" --days 2 --size 4096

import os
import os.path
import shutil
import datetime
import argparse
from glob import glob


parser = argparse.ArgumentParser(description='Parser for Exercise 6')
parser.add_argument('--source', type=str, default=None, help='Enter the full path to directory')
parser.add_argument('--days', type=int, default=2, help='Enter the different between date creation of files')
parser.add_argument('--size', type=int, default=None, help='Enter the size of files that needs to put lower than size')
my_parser = parser.parse_args()


def last_modified(filename):
    t = os.path.getctime(filename)
    print(1)
    return datetime.datetime.fromtimestamp(t)


def reorganize(source=my_parser.source, days=my_parser.days, size=my_parser.size):
    os.chdir(source)

    now = datetime.datetime.now()

    files_and_dirs = [i for i in os.listdir(os.getcwd())]
    files = list(filter(None, [i if os.path.isfile(i) else None for i in files_and_dirs]))
    dirs = list(filter(None, [i if os.path.isdir(i) else None for i in files_and_dirs]))

    if os.path.exists('Archive'):
        shutil.rmtree('Archive')
    if 'Small' in dirs:
        shutil.rmtree('Small')

    os.mkdir('Archive')
    os.mkdir('Small')

    for file in files:
        file_created = last_modified(file)
        tmp = file_created.day
        if tmp + days > now.day:  
            shutil.move(file, source + '\\Archive')
        elif os.path.getsize(file) < size:  
            shutil.move(file, source + '\\Small')


reorganize()

