import csv
import re

with open('hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = []
    regex = r'[Pp]ython'
    for row in csv_reader:
        if re.search(regex, row[1]) or re.search(regex, row[2]):
            line_count.append(row)
    print(f'The numbers of lines with Python are {len(line_count)}')
