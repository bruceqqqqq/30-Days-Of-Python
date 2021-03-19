# 'r' read only, value default, error if file doesn't exist
# 'a' append, if file doesn't existe this will create it, and can you appending info into it
# 'w' write, opens a file for writting in it, creates if doesn't exist
# 'x' create, create a file, error if already exist
# 't' text, default value, text mode
# 'b' binary, binary mode (ex: images)
# 'w+' Opens a file for writing and reading

f = open('txt_example.txt')
# line = f.readline()
# list_of_lines = f.readlines() # show \n
# f.read().splitlines() # dont show \n
# txt = f.read(10)
# txt = f.read()
# print(txt)
# print(type(txt))
line = f.readline()
print(line)
f.close()
