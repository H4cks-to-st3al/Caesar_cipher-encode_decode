chars=['ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz']

def encoding(message,shift=4):
    encr_text=str.maketrans(
        f'{chars[0]}{chars[1]}',
        f'{chars[0][shift:]}{chars[0][:shift]}{chars[1][shift:]}{chars[1][:shift]}'
    )
    return str.translate(message,encr_text)

def decoding(message,shift=4):
    decr_text=str.maketrans(
        f'{chars[0][shift:]}{chars[0][:shift]}{chars[1][shift:]}{chars[1][:shift]}',
        f'{chars[0]}{chars[1]}'
    )
    return str.translate(message,decr_text)

opt=input(('Select [E]ncoding or [D]ecoding: '))
if opt == 'E':
    message=input('Enter the plain text: ')
    shift=int(input('Enter the shift key in between[1-26]: '))
    if shift < 1 or shift > 26:
        raise Exception (f'Invalid input',shift)
    else:
        print(f'Your Cipher text: {encoding(message,shift)}')
elif opt == 'D':
    message=input('Enter the Cipher text: ')
    shift=int(input('Enter the shift key in between[1-26]: '))
    if shift < 1 or shift > 26:
        raise Exception (f'Invalid input',shift)
    else:
        print(f'Your decoded text: {decoding(message,shift)}')