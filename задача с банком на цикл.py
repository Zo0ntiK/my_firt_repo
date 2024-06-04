prozent = int(input('под какой процент вы кладёте деньги:'))
money = int(input('колько денег вы положите в банк:'))
year = int(input('на сколько лет вы хотите положить деньги в банк:'))
prozent_number = prozent / 100
for i in range(year):
    money_in_year = money * prozent_number
    money = money + money_in_year  
    print(f'год {i+1} на вашем счету {money} ')

print(f'ваш итоговый счёт: {money}')
    
