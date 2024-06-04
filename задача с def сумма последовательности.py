def seqence_sum(a,s,d):
    my_sum = 0 
    for i in range(a,s + 1,d ):
        my_sum += i
    return my_sum
        


print(seqence_sum(2,6,2))
print(seqence_sum(1,5,1))
print(seqence_sum(16,15,3))
print(seqence_sum(1,6,2))
