# CIL-Academy-Python-Challenge

## Cryptography Challenge 

Cryptography, or cryptology is the practice and study of techniques for secure communication. Cryptography relies on using more or less complex encryption 
algorithms to encode a readable message (plaintext) into a collection of characters (ciphertext) that is hard to decipher (decode).

### The Python Code 
```#Cryptography Challenge #1
import random, time
#A basic encryption algorithm...
def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciphertext = ""
  for i in range(0,len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range (0,key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext
#Main program starts here...
#Input...
plaintext = input("Enter a message to encrypt (plaintext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
  print("Invalid key, try again!")
  key = int(input("Input a key as a number between 1 and 10"))
  
#Process... 
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)
#Output...
print("Ciphertext:")
print(ciphertext)```

## The Challenge
Your first task is to **reverse-engineer** this code to understand how this encryption algorithm works. 
Then, your challenge consists of writing a new function called **decrypt()**, that takes two parameters (a **ciphertext** and a **key**) and returns the **plaintext**
corresponding to the given ciphertext.
Update the table below with the answers obtained from your decrypt() function

### Decryption Table
Using your new **decrypt()** function, decrypt the following messages:


![image](https://user-images.githubusercontent.com/97846257/227604128-978427aa-4b14-48a8-ab65-e12aa7ef11ef.png)

## Example Run
![image](https://user-images.githubusercontent.com/97846257/227604345-dc6b145d-9a80-41c0-b19f-03d74ed9afd0.png)

