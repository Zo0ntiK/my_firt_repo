print('выберете напрвление налево-направо')
print("ваше положение '_','*','_' ")
variant = input('напишите выход для завершения :')
pole = ['_','*','_']

start = 1
while True:
    
   if variant == 'направо':      
       
       start += 1
       
       pole[start] = '*'
       pole[start - 1] = '_'
       
       
       print(pole)
       variant = input('напишите выход для завершения :')

   elif variant == 'налево':
       
       start -= 1
       
       pole[start] = '*'
       pole[start + 1 ] = '_'
       
       
       print(pole)
       variant = input('напишите выход для завершения :')

   if  pole == ['_','_','*'] and variant == 'направо' or pole  == ['*','_','_'] and variant == 'налево':
       print('вы за приделами поля ')
       break
       

   if variant == 'выход':
       print(f'текущее положение {pole}')
       break
    
  
