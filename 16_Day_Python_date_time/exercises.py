from datetime import  datetime
from datetime import time
from datetime import date

current = datetime.now()
current_strftime = current.strftime("%d/%m/%Y %H:%M:%S")
day, month, year, hour, minute, timestamp = current.day, current.month, current.year, current.hour, current.minute, current.timestamp()
print(day, month, year, hour, minute)
print(current_strftime)
print('Actual Timestamp:', timestamp)

date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, '%d %B, %Y')
print(date_object)

today = date(year=2021, month=2, day=10)
new_year = date(year=2022, month=1, day=1)
time_left_for_a_new_year = new_year - today
print(time_left_for_a_new_year)

datefrompast = date(year=1970, month=1, day=1)
diff = today - datefrompast
print(diff)


