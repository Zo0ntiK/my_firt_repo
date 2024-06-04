def find_average(number):
    quantity  = len(number)
    my_number = 0
    for i in number:
        my_number += i
        
    if number == []:
        return 0 
    return my_number / quantity


number = []
print(find_average([1,2,3,5]))
print(find_average([7,7,7]))
print(find_average([]))
