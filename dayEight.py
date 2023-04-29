alphabets = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text,shift):
    encryptedMessage = ""
    for letter in text:
        position = alphabets.index(letter) + shift
        if (position > 26):
            position = position - 26
        encryptedMessage += alphabets[position]
    return encryptedMessage

def decrypt(text, shift):
    decryptedMessage = ""
    for letter in text:
        position = alphabets.index(letter) - shift
        decryptedMessage += alphabets[position]
    return decryptedMessage

decision = True
while decision is True:
    code = input("Type 'encode' to encrypt, or 'decode' to decrypt: ")
    text = input("Enter The Text Message: ")
    shift = int(input("Enter A Shift Number: "))

    if code == "encode":
        result = encrypt(text, shift)
        print(f"Here Is The Encoded Result: {result}")
    elif code == "decode":
        result = decrypt(text, shift)
        print(f"Here Is The Decoded Result: {result}")

    direction = input("Type 'yes' if you wish to continue, or 'no' if you wish to exit the game? ")
    if direction == "no":
        break