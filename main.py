#Wendy Vallejos

password = None
#encode password as encoded password
def encode(password):
    epassword = ""
    for x in password:
        ex = str((int(x) + 3))
        epassword += ex
    return epassword

def decode(password):
    edp = ""
    for x in password:
        edp += str((int(x) - 3))
    return edp

#display menu with the options
def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        num = int(input('Please enter an option:'))
        #encodes the orignal password
        if num == 1:
            password = input('Please enter your password to encode:')
            print('Your password has been encoded and stored!')
            password = encode(password)

        elif num == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')

        elif num == 3:
            break

if __name__ == '__main__':
    main()