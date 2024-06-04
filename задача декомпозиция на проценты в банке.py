savings = int(input('ввведите сумму'))
interest = (int(input('введите процент'))) / 100
time = int(input('ввведите время '))

def calculate_savings (savings,interest,time):
    '''
    input: savings - data about money,interest - data about percent,time data about time
    return:int
    '''
    for i in range(time):
        savings += savings * interest
    return savings
    
    
def bank (s,i=0.2,t=1):
    '''
    input:calculate_savings(s,i,t) s - data about money,i - data about percent,t - data about time
    return:bool or int
    '''
     if i*100 > 5:
         print('максимальный процент в нашем банке 5% годовых')
         return False
     savings = calculate_savings(s,i,t)
     return savings

total_saving = bank (savings,interest,time)
if total_saving:
    print(f'ваш итоговы счёт в банке: {total_saving}')

