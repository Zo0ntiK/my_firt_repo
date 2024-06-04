question = (
           ('Я - вода и по воде плаваю. Кто я?', 'льдина'),
           ('Все меня топчут, а я - всё лучше.', 'тропинка'),
           ('Что невозможно удержать и десяти минут, хотя оно легче пёрышка?', 'дыхание'),)
def riddle (s,a):
    return s.lower() == a.lower()
print('разгадайте 3 загадки')
count = 1
for q in question:
    print(f'{count}- загадка')
    print(f'{q[0]}')
    my_input = input('ваш ответ:')
    
    if riddle (q[1],my_input):
        print(f'ответ {my_input} правильный ')
    else:
        print(f'ответ неверный {my_input} правильный овет: {q[1]}')
    count += 1
    
