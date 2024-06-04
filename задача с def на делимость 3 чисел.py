def is_div(x,y,z):
    return x % y == 0 and x % z == 0
    
print(is_div(x=4,y=2,z=1))
print(is_div(x=12,y=3,z=4))
print(is_div(x=7,y=7,z=2))

def is_div_v2(x,y,z):
    return not x % y and not x % z
