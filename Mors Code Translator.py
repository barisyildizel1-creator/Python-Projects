MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            letter = letter.upper()
            if letter in MORSE_CODE_DICT:
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                print(f"Warning: Character '{letter}' not supported, skipping...")
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    i = 0
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                if citext in MORSE_CODE_DICT.values():
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                    .values()).index(citext)]
                else:
                    print(f"Warning: Morse code '{citext}' not found, skipping...")
                citext = ''
    return decipher

message = (input("Enter the message: ")).capitalize()
choice = input("Type '1' to encrypt or '2' to decrypt: ")
if choice == '1':
    print("Encrypted message:", encrypt(message))
elif choice == '2':
    print("Decrypted message:", decrypt(message))
else:
    print("Invalid choice")