time = ['1:34:35','5:56:40','5:22:50']


hours_counter = 0 
minutes_counter = 0
seconds_counter = 0

for index in range(len(time)):
    parsed_time = time[index].split(':')
    
    hours = int(parsed_time[0])
    minute = int(parsed_time[1])
    seconds = int(parsed_time[2])

    hours_counter += hours
    minutes_counter += minute
    seconds_counter += seconds
    
print(hours_counter)
print(minutes_counter)
print(seconds_counter)
    
if seconds_counter >= 60:
    minutes_counter += seconds_counter // 60
    seconds_counter = seconds_counter % 60
    
if minutes_counter >= 60:
    hours_counter += minutes_counter // 60
    minutes_counter = minutes_counter % 60    
    
    
    
print(f'часы: {hours_counter}')
print(f'минуты: {minutes_counter}')
print(f'секунды: {seconds_counter}')
    
    
