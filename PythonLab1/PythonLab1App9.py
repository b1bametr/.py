def baks():
    money_in_stock = {1000: 2, 500: 2, 200: 10, 100: 5, 50: 5, 10: 20}
    result = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 10: 0}
    money = 5370
    for key in money_in_stock.keys():
        current = money // key 
        if current > money_in_stock[key]:
            money = money - (money_in_stock[key] * key)
            result[key] = money_in_stock[key]
        else:
            money = money % key
            result[key] = current
    print("Ваши деньги : " + str(sum([k * v for k, v in zip(result.keys(), result.values())])))
    print(result)


cashDispenser()
