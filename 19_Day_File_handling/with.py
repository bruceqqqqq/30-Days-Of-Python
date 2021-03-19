import os

# with open('txt.txt', 'r') as f:
#     line = f.read().splitlines()
#     print(line) # Better list
#
# with open('txt.txt', 'a') as f:
#     f.write('This text has to be appended at the end of file.')
#
# with open('txt1.txt', 'w') as f:
#     f.write('This text will be written in a newly file')

# if os.path.exists('txt.txt'):
#     os.remove('txt.txt')
#
# if os.path.exist('txt1.txt'):
#     os.remove('txt1.txt')

skills = ['Python', 'Gaming', 'Fuck']
with open('txt_example.txt', 'w') as file:
    for s in skills:
        file.write(s+'\n')
