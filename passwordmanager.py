from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

    

def view():
    with open('passwords.txt', 'r') as f: # 'r' mode just allows us to read the file
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|') #.split() splits the info every time it reads '|' into a list
            print(f'User:', user, '| Password:', fer.decrypt(passw.encode()).decode()) #decode() gets ride of the b'' (the bytes) in the text

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f: #passwords.txt is the file, 'a' mode allows you to add something to the end of an existing file and create a new one if that file does not exist.
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input('Would you like to add a new password or view existing ones? (view, add) (press q to quit) ').lower()
    if mode == 'q':
        break
    if mode =='view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue