weather = input('укажите погоду-солнечно или пасмурно? ').lower()
temp =  int(input('какая температура? '))
if weather == 'солнечно' :
    print('зонт брать не стоит')
elif weather == 'пасмурно' and temp >= 0:
    print('возьмите зонт ')
elif weather == 'пасмурно' and temp <  0:
    print('возьмите зонт , могут быть осадки ')


