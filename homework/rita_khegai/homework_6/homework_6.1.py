# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero” и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова. Если после слова идет запятая или точка,
# этот знак препинания должен идти после того же слова, но уже преобразованного.

print('Задание 1')
print()

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
        'facilisis vitae semper at, dignissim vitae libero')
text = text.split()
currect_text = []

for word in text:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
        currect_text.append(word)
    elif word.endswith('.'):
        word = word.replace(',', 'ing.')
        currect_text.append(word)
    else:
        word = word + 'ing'
        currect_text.append(word)
print(' '.join(currect_text))