number = int(input('введите размер для шаблона: '))
template = []

for i in range(number):
    template.append('_')
for w in range(1,number + 1):
    template[-w ] = '*'
    template[-w + 1] = '_'
    print(template)
    
