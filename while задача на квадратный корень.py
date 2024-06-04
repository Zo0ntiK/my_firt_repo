kor = int(input('введите число которого хотите найти квадратный корень '))
number = int(input('ведите число '))

while  number * number != kor :  
     number += 1
number = (number + kor / number) / 2
print(f' {number} квадратный корень {kor}')

    
