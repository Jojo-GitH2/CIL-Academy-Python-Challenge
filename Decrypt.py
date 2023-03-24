# Decrypting
import time
def decrypt(ciphertext, key):
    # Start out with an empty string
    plaintext = ""
    # Loop through the ciphertext in steps equivalent to the key value
    for i in range(0, len(ciphertext), key + 1):
        plaintext += ciphertext[i]
        
    return plaintext

ciphertext = input("Enter a message to encrypt (ciphertext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))
#Process... 
print("...")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)
plaintext = decrypt(ciphertext, key)
#Output...
print("Plaintext:")
print(plaintext)
        
