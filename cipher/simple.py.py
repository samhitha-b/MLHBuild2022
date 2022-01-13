def encrypt(message):

    result = ''

    for letter in message:
        converted = ord(letter) + 13
        result = result + converted
    
    print("Message after encryption: ")
    print(result)


def decrypt(message):

    original = ''

    for letter in message:
        converted = ord(letter) - 13
        original = original + converted
    
    print("Message after decryption: ")
    print(original)

choice = int(input("Enter 1. To encrypt a message\n2. To decrypt a message"))
user = input("Enter the message")
if choice == 1:
    encrypt(user)
elif choice ==2:
    decrypt(user)
else:
    print("Input error, try again")