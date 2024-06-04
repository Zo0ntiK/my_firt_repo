run = int(input('введите скорость автомобиля '))
distance = int(input('введите растояние '))
dele = distance / run
if dele >= 1 :
    print(f'время за которое автомобиль преодолеет дистанцию в {distance} км,'
          f'за время { dele } ')
    print ('он не успеет за 1 час')
else  :
    print(f'время за которое автомобиль преодолеет дистанцию в {distance} км,'
          f'за время {dele} ')
    print ('он успеет за 1 час')
