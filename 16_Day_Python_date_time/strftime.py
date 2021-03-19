from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
print(f'Time: {t}')

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f'Time one: {time_one}')

date_string = '10 February, 2021'
print(f'Date_string = {date_string}')

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
