def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
my_input = input('введите слово:')

if palindrome(my_input):
    print(f'слово {my_input} - палиндром')
else:
    print(f'слово {my_input} - не палиндром')
