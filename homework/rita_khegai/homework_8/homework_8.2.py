# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число


import sys


def progression(limit=10000001):
    m = 1
    n = 1
    count = 1
    while count < limit:
        yield m
        yield n
        m += n
        n += m
        count += 1


sys.set_int_max_str_digits(100000)


meter = 1
for number in progression(100000):
    if meter == 5:
        print(number)
    elif meter == 200:
        print(number)
    elif meter == 1000:
        print(number)
    elif meter == 100000:
        print(number)
    meter += 1
