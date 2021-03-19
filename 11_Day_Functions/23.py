import keyword

def check_print(var: str):
    if keyword.iskeyword(var):
        print('Cannot be a variable because is a keyword')
    elif not keyword.iskeyword(var):
        print('This is not a keyword')
    if var.isidentifier():
        print('Can be a variable')
    else:
        print('Can not be a variable')
    print()

check_print('123')
check_print('teste')
