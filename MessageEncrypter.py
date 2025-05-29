import sys

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(message,shift):
    EncryptedLetter=""
    for letter in message:


        shiftedIndex = (alphabet.index(letter)+shift)%26


        EncryptedLetter += alphabet[shiftedIndex]






    print(f"Your encrypted message is:  {EncryptedLetter}")


def decrypt(message,shift):
    DecryptedLetter=""
    for letter in message:
        shiftedIndex = (alphabet.index(letter)-shift)%26

        DecryptedLetter += alphabet[shiftedIndex]

    print(f"Your decrypted message is:  {DecryptedLetter}")

while True:
    while True:
        print("---------------Welcome to the Message Encrypter---------------------------")
        actionDeterminer=input("Type 'encode' to encrypt ,  'decode' to decrypt or  ex to Exit: = ").lower()
        if not actionDeterminer.isalpha():
            print("Invalid input")

        elif actionDeterminer not in ["encode","decode","ex"]:
            print("Invalid Choice ")

        elif actionDeterminer=="encode":





            while True:
                message = input("Type your message:").lower()
                if not message.isalpha():
                    print("Invalid input")
                elif message.isalpha():
                    break




            while True:
                shift = input("Type the shift number:")
                if not shift.isdigit():
                    print("Invalid input")
                elif shift.isdigit():
                    break

            encrypt(message,int(shift))
            break





        elif actionDeterminer=="decode":
            while True:
                message = input("Type your message:").lower()
                if not message.isalpha():
                    print("Invalid input")
                elif message.isalpha():
                    break




            while True:
                shift = input("Type the shift number:")
                if not shift.isdigit():
                    print("Invalid input")
                elif shift.isdigit():
                    break
            decrypt(message,int(shift))


        elif actionDeterminer=="ex":
            sys.exit()


