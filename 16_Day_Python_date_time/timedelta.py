from datetime import timedelta

t1 = timedelta(weeks=12, hours=23)
t2 = timedelta(days=34, hours=2, minutes=20, seconds=1, microseconds=1, milliseconds=111)
t3 = t1 - t2
print(t3)
