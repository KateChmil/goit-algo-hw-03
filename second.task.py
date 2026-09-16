import random 

def get_numbers_ticket(min, max, quantity):
    list = []
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        print("Пустий список", list)
        return sorted(list)

    for el in range(quantity):
        num = random.randint(min, max)
        while num in list:
            num = random.randint(min, max)
        list.append(num)
    print("Список чисел:", sorted(list))
    return sorted(list)

get_numbers_ticket(2, 60, 3)
get_numbers_ticket(1, 10, 5)

get_numbers_ticket(0, 6000, 8)
get_numbers_ticket(1, 10000, 5)

get_numbers_ticket(700, 780, 20)
get_numbers_ticket(30, 45, 5)

