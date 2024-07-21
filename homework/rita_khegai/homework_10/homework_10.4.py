PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# При помощи генераторов превратите этот текст в словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}

dictionary = {}
price_list1 = PRICE_LIST.splitlines()
price_list2 = [elem[:-1] for elem in price_list1]

for pair in price_list2:
    key, value = pair.split()
    dictionary[key] = int(value)

print(dictionary)
