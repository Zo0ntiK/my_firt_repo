def generete_shape(s):
    plus_list = ''
    for i in range(s):
        plus_list += '+'
    plus_list +='\n'
    return (plus_list * s)[:-1] 
        

def generete_shape_v2(n):
    return (('+'*n + '\n')*n )[:-1]




print(generete_shape(2))
print(generete_shape(3))
print(generete_shape(0))
