from random import randint
number = randint(1,100)
print('попробуй угадать число от 1 до 100')

def user_number():
    return int(input('ваше предложение:'))     
def true_variant(s):
    if s == number:
        return True
def more_number (e):
    if e < number:
        return True
def few_number(r):
    if r > number:
        return True

while True:

    
    user_input = user_number()
    if true_variant(user_input):
        print('ответ верный')
        break
    elif more_number(user_input):
        print(f'ответ неверный,попробуйте число больше чем {user_input}')
    elif few_number(user_input):
        print(f'ответ неверный,попробуйте число меньше чем {user_input}')

 

    
        






