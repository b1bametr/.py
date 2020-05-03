def non_empty(func):
    def dec():
        result = func()
        return list(filter(None, result))

    return dec

@non_empty 
def get_pages():
    return [None, 'Глава 1', '', 1, 'содержание', '', 'линия 1', None]

print(get_pages())