def extra_enumerate(x):
    cum = 0
    fraction = 0
    for step in x:
        fraction += step
    for i in range(len(x)):
        elem = x[i]
        cum += x[i]
        frac = cum / fraction
        yield i, elem, cum, round(frac, 1)


x = [i for i in range(15)]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
