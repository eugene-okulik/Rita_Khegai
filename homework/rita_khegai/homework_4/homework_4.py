my_dict = {
    'tuple': (1, 56.6, 5, None, -3, '2024'),
    'list': [33, 'kak dela?', 'rita', 148.888765, 'platie', False],
    'dict': {1: 'odin', 2: 'dva', 3: 'tri', 4: 'chetire', 5: 'pyat'},
    'set': {1, 2, 3, 4, 5, 6}
}


# Раздел "Кортеж"
tuple_ = my_dict['tuple']
last_items_tuple = tuple_[-1]

# Раздел "Список"
list_ = my_dict['list']
list_.append('Privetiki')
last_items_list = list_[-1]
deleted_items_list = list_.pop(1)

# Раздел "Словарь"
dict_ = my_dict['dict']
dict_['i am a tuple'] = 'Super puper'
deleted_items_dict = dict_.pop(3)

# Раздел "Множество"
set_ = my_dict['set']
set_.add('Pomidor')
set_.discard(3)

symbol_ = ' _ '
symbol_ *= 3
print('1) Последний элемент кортежа   ' + symbol_ + str(last_items_tuple) + symbol_)

print('2) В список добавлен элемент   ' + symbol_ + str(last_items_list) + symbol_)
print('3) Из списка удален элемент   ' + symbol_ + str(deleted_items_list) + symbol_)

print('4) В словарь добавлен элемент со значением   ' + symbol_ + str(dict_['i am a tuple']) + symbol_)
print('5) Из словаря удален элемент со значением  ' + symbol_ + str(deleted_items_dict) + symbol_)

print(
    '6) Во множество добавлен элемент  ' + symbol_ + 'Pomidor' + symbol_ + 'и удален элемент ' + symbol_ + '3' + symbol_
)

print(my_dict)