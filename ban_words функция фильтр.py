def word_filter(my_words):
    return_list = []
    
    for i in my_words:
        for w in ban_words:
            if  i == w  :
                my_words.remove(w)
                
       
    return my_words
                
                
my_words = []
ban_words = ['hello','world','strange']
print(word_filter(['hello','my','name']))
print(word_filter(['world','is','beautiful']))
print(word_filter(['no','banned']))

def word_filter_v2(my_words):
    res = []
    for i in words:
        if i not in ban_words:
            res.append(i)
    return res
