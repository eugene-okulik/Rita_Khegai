# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

import sys


n = 1
m = 1
fibonachi = [n, m]

while len(fibonachi) < 100001:
    n = n + m
    m = n + m
    fibonachi.append(n)
    fibonachi.append(m)

sys.set_int_max_str_digits(100000)

print(fibonachi[5])
print(fibonachi[200])
print(fibonachi[1000])
print(fibonachi[100000])
