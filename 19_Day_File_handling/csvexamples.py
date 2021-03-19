import csv

with open ('csv_example.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} is a teachers. He lives in {row[1]}, {row[2]}')
            line_count += 1
    print(f'Number of lines: {line_count}')
