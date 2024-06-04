def array_plus_array(my_list,your_list):
    my = 0
    your = 0
    for i in my_list:
        my += i
    for w in your_list:
        your += w
    return my + your

my_list = []
your_list = []
print(array_plus_array([1,2,3],[4,5,6]))
print(array_plus_array([0],[0]))
print(array_plus_array([-1,-2],[-3,-4]))
