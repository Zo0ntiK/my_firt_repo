def find_smallest_int(numbers):
    if numbers == []:
        return 0
    number = 0
    number += numbers[0]
    for i in numbers:
        if i < number:
            number = i
    return number
        
            
                
numbers = []
print(find_smallest_int([34,15,88,2]))
print(find_smallest_int([34,-345,-1,100]))
print(find_smallest_int([0]))
