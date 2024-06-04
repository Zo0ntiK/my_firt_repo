def century(s):
    year_v1 = s // 100
    year_v2 = 0
    if s % 100 != 0:
        year_v2 += 1
    return year_v1 + year_v2
print(century(1705))
print(century(1900))
print(century(89))
        
def century_v2(year):
    if not year % 100:
        return year // 100
    return year // 100 + 1
    
    
