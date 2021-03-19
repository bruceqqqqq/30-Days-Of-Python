score = int(input('Enter your score: '))
if 80 <= score <= 100:
    print('This student receive A')
elif 70 <= score <= 79:
    print('This student receive B')
elif 60 <= score <= 69:
    print('This student receive C')
elif 50 <= score <= 59:
    print('This student receive D')
elif 0 <= score <= 49:
    print('This student receive F')
else:
    print('Invalid input')