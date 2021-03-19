import pandas as pd
import numpy as np

# 1
df = pd.read_csv('hacker_news.csv')
# 2
first_five = df.head(5)
# 3
last_five = df.tail(5)
print('First Five Rows\n', first_five)
print('Last Five Rows\n', last_five)

# 4
titles = pd.Series(df.columns)
print(titles,'\n')
# 5
print('Rows:', len(df), 'Columns:', len(df.columns))
# 5 A
print('Rows with Python:\n', df[df['title'].str.contains('[Pp]ython')])
# 5 B
print('Rows with JavaScript:\n', df[df['title'].str.contains('JavaScript')])
# 5 C
python_rows_title = df[df['title'].str.contains('[Pp]ython')]
print('Read some info by Python:')
for p in python_rows_title.values:
    print(p[1], p[2])
