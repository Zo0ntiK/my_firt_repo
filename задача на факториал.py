number = int(input('введите число: '))
result = 1
for i in range(1,number + 1):
    result *= i 


print(f'вакториал числа - {number} равен {result}')
