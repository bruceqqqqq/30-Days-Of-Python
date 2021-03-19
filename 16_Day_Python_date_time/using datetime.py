from datetime import datetime
now = datetime.now()
print(now)
second = now.second
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year
timestamp = now.timestamp()
exampleoftimestamp = datetime.fromtimestamp(1612968912.318157)
print(f'{day}/{month}/{year} {hour}:{minute}:{second}')