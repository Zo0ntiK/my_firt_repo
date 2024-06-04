word = input('введите слово :')
glas = 0
cogl = 0

for i in word:
    if i== 'а' or i== 'у' or i== 'о' or i== 'ы' or i==  'и' or i==  'э' or i== 'я' or i== 'ю' or i== 'ё' or i==  'е' :
        glas += 1
    elif i == 'ъ' or i== 'ь':
        print(f'{i} не гласный и не согласный его не считаем')
    else:
        cogl += 1

print(f'в слове {word}')
print(f'гласных: {glas}')
print(f'согласных: {cogl}')





word = input('ведите слово:')
vowels = 'ауоыэияюёе'
vowel_counter = 0

for i in word:
    for v in vowels:
        if i == v:
            vowel_counter += 1

consonant_counter = len(word) - vowel_counter

print(f'в слове {word} кол-во'
'гласных {vowel_counter}'
'согласных {consonant_counter}')
