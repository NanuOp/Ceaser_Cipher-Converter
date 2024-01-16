"""Ceaser Cipher"""
def cipher(message,key, mode):
    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                offset = 65
            else:
                offset = 97
            encrypted_message+=chr((ord(letter)-offset+key*mode)%26+offset)
        else:
            encrypted_message+=letter
    return encrypted_message
def encrypt(message, key):
    return cipher(message, key, 1)
def decrypt(message, key):
    return cipher(message, key, -1)


"""MAIN"""

opt= int(input("Enter 1 to encrypt a message and 2 to decrypt a message: "))
if opt==1:
    message = input("Enter the message: ")
    key= int(input("Enter your encryption key: "))
    if message!="":
        encrypted= encrypt(message, key)
        print(f"The encrypted message is {encrypted}")
        
    else:
        print("Empty messages cannot be encrypted!!!")
elif opt==2:
    message = input("Enter the message: ")
    key= int(input("Enter your decryption key: "))
    if message!="":
        decrypted= decrypt(message, key)
        print(f"The decrypted message is {decrypted}")
        
    else:
        print("Empty messages cannot be decrypted!!!")

else:
    print("Invalid Input!!!")