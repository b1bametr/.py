#Напишите декоратор non_empty, который дополнительно проверяет
#списковый результат любой функции: если в нем содержатся пустые
#строки или значение None, то они удаляются. Пример кода:


def non_empty(func):
    def dec():
        result = func()
        return list(filter(None, result))

    return dec

@non_empty 
def get_pages():
    return [None, 'Глава 1', '', 1, 'содержание', '', 'линия 1', None]

print(get_pages())