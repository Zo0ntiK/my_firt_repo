print('что вы хотите добавить в список')
my_list = input('если вы закончили то напишите -выход: ').lower()
shopping_list = [my_list]
print(shopping_list)
while True:
    if my_list == 'выход':
        shopping_list.remove('выход')
        print(f'ваш итоговый список {shopping_list}')
        
        break
          
    else:
        my_list = input('если вы закончили то напишите -выход: ').lower()
        shopping_list.append(my_list)
        
        print(shopping_list)
    
    
    
