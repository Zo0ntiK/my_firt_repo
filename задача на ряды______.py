place = input('введите ряд в символах * или _ :')
while True:
    my_list = place.count('*')
    print(f'кол-во свободных мест в ряду {place}')
    print(f'равен {my_list}')
    break






row = '*__*_'
empty_row = 0

for i in row:
    if i == '*':
        empty_row += 1

print(f'кол-во свободных мест в ряду {row} равняется {empty_row}')
