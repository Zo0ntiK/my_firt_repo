x = int(input('введите число'))
y = 1
prev_number = y
while True:
    if y * y == x:
        print(f'квадратный корень из  числа {x} равен {y}')
        break
    else:
        prev_number = y
        y = (y + x / y) / 2
        
        if prev_number == y :
           print(f'самый приблежёный квадратный корень числа {x} равен {prev_number}')
           break
