number = int(input('введите размер для шаблона: '))
template = []

for i in range(number):
    template.append('_')
for w in range(number ):
    template[w] = '*'
    template[w - 1] = '_'
    print(template)
    
