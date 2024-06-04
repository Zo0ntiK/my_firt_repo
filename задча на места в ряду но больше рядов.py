movie_seats = [
    '*___',
    '****',
    '_*__'
    ]
free_sets = 0
for i in movie_seats:
    for w in i:
        if w == '*':
            free_sets += 1
print(f'свободных мест в кинотеатре - {free_sets}')
                
            
        
    
