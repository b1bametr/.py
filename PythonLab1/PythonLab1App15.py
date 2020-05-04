#Напишите параметризированный декоратор pre_process, который
#осуществляет предварительную обработку (цифровую фильтрацию)
#списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
#коде (по умолчанию равен 0.97). Пример кода:



def pre_process(a=0.97):
    def decorator(func):
        def wrap(*args):
            s = args[0]
            for i in range(1, len(s)):  
                s[i] = s[i] - a * s[i - 1]  
            print('a = ', a)
            func(s)

        return wrap

    return decorator

@pre_process(a=0.95)
def plot_signal(s):
    for sample in s:
        print(sample)

arr = [i for i in range(10)]
plot_signal(arr)
