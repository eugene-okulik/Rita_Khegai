# Задание 1
# Дан такой список:
# person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
person2 = f'Имя персоны: {name}, Фамилия: {last_name}, Страна/город проживания: {country}/{city}, Телефон: {phone}.'
print('Задание 1')
print(person2)
print(' ')


# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'

a_index = a.index(':') + 2
b_index = b.index(':') + 2
c_index = c.index(':') + 2

d = a[a_index:]
e = b[b_index:]
f = c[c_index:]

d = int(d) + 10
e = int(e) + 10
f = int(f) + 10

print('Задание 2')
print(f'Результат сложения равен {d}')
print(f'Результат сложения равен {e}')
print(f'Результат сложения равен {f}')
print(' ')


# Задание 3
# Даны такие списки:
# students = ['Ivanov', 'Petrov', 'Sidorov']
# subjects = ['math', 'biology', 'geography']
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Задание 3')
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
