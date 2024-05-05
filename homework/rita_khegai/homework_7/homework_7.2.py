# Дан такой словарь:
# words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# Выведите на экран каждый ключ столько раз сколько указано в значении. Т.е. как-то так:
# III
# lovelovelovelove
# итд
# Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

a, b, c, d = words.items()

a1, a2 = a
b1, b2 = b
c1, c2 = c
d1, d2 = d


def print_key(key, value):
    print(key * value)


print_key(a1, a2)
print_key(b1, b2)
print_key(c1, c2)
print_key(d1, d2)
