# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
#     10000, True - '$10255'
#     25000, False - '$25000'
#     600, True - '$3785'

import random

salary = int(input("Введите число: "))
bonus = bool(random.getrandbits(1))
random_num = random.randrange(2, 20)
salary_bonus = salary * random_num

if bonus == True:
    print(str(salary) + ", " + str(bonus) + " - '$" + str(salary_bonus) + "'")
else:
    print(str(salary) + ", " + str(bonus) + " - '$" + str(salary) + "'")
