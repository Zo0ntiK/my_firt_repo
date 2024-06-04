def update_light(s):
    s = s.lower()
    if s == 'green':
        return 'yellow'
    elif s ==  'yellow':
        return 'red'
    else:
        return 'green'
print(update_light('Green'))
print(update_light('Yellow'))
print(update_light('Red'))
