from datetime import date, datetime

# 1 example
today = date(year=2021, month=2, day=10)
new_year = date(year=2022, month=1, day=1)
time_left_for_a_new_year = new_year - today
print(f'Time for a new year {time_left_for_a_new_year}')

# 2 example
t1 = datetime(year=2021, month=2, day=10, hour=1, minute=2, second=3)
t2 = datetime(year=2022, month=1, day=1, hour=10, minute=20, second=3)
t3 = t2 - t1
print(f'Time for a new year #2 {t3}')