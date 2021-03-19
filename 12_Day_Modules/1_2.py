import string
import secrets

def random_user_id():
    char = string.ascii_letters + string.digits
    id = ''.join(secrets.choice(char) for i in range(6))
    return id

def user_id_gen_by_user():
    char = string.ascii_letters + string.digits
    charinput = int(input('Number of characteres: '))
    charids = int(input('Number of IDs: '))
    id = list()
    for i in range(charids):
        id.append(''.join(secrets.choice(char) for i in range(charinput)))
    return ' '.join(id)

print(random_user_id())
print(user_id_gen_by_user())