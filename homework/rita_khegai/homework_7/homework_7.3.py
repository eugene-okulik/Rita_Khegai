# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 54
# результат работы программы: 209
# результат: 2
# Нужно сделать всё то же самое, но уже способ - на ваше усмотрение
# (можно с помощью срезов и метода index, а можно с помощью split ).
# Получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте. Главное отличие - выполните всё с использованием функций.
# Нужно сделать так, чтобы строк кода стало как можно меньше, и не было повторений одного и того же.

a = "результат операции: 42"
b = "результат операции: 54"
c = "результат работы программы: 209"
d = "результат: 2"


list_a = a.split()
list_b = b.split()
list_c = c.split()
list_d = d.split()


def last_value(string):
    return string[-1]


last_value_a = last_value(list_a)
last_value_b = last_value(list_b)
last_value_c = last_value(list_c)
last_value_d = last_value(list_d)


def result(last_value_int):
    print(int(last_value_int) + 10)


result(last_value_a)
result(last_value_b)
result(last_value_c)
result(last_value_d)
