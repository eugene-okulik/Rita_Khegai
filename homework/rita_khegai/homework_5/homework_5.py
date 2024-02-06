# Задание 1
# Дан такой список:
# person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]
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

d = a.split()
e = b.split()
f = c.split()

d = d[2]
e = e[2]
f = f[3]

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
