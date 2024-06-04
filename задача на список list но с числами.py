print('какую игру вы хотите добавить в список ')
my_game = input('если вы закончили напишите выход :').lower()
reyting = int(input('какой у этой игры рейтинг:'))
my_list = [ (my_game,reyting)]
print(my_list)
while True:
    if my_game == 'выход':
        my_list.pop(-1)
        print(f'ваш итоговый список {my_list}')
        break
    else:
        my_game = input('сли вы закончили напишите выход :').lower()
        reyting = int(input('какой у этой игры рейтинг:'))
        my_list.append((my_game,reyting))
        print(my_list)
