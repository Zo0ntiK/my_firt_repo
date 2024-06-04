name = input('введите название ')
name_len = len(name)
if name_len ==0:
    print(f'{name_len}-{name} вы написали ничего')
elif name_len >= 1 and name_len <= 3:
    print(f'{name_len}-{name} слишком короткое название')
elif name_len >= 3 and name_len <= 7:
    print(f'{name_len}-{name} идеальное название ')
else:
    print('слишком длиное')
