'''
XOR decryption
-------------------
Problem 59

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

'''

import itertools as it
import string as s

def decript2(message, keys):
    k0, k1, k2 = keys[0], keys[1], keys[2]
    dec = []
    aValue = 0
    aSum = 0
    for i in range(0, len(message), 3):
        aValue = int(message[i  ])^ord(k0)
        aSum += aValue
        dec += chr(aValue)
        aValue = int(message[i+1])^ord(k1)
        dec += chr(aValue)
        aSum += aValue
        aValue = int(message[i+2])^ord(k2)
        dec += chr(aValue)
        aSum += aValue

    d = ''.join(dec)
    print(d)
    return aSum

def foundCipherKey(message):
    for k0, k1, k2 in it.product(s.ascii_lowercase, repeat=3):
        dec = []
        aValue = 0
        aSum = 0
        for i in range(0, len(message), 3):
            aValue = int(message[i  ])^ord(k0)
            aSum += aValue
            dec += chr(aValue)
            aValue = int(message[i+1])^ord(k1)
            dec += chr(aValue)
            aSum += aValue
            aValue = int(message[i+2])^ord(k2)
            dec += chr(aValue)
            aSum += aValue

        d = ''.join(dec)
        if set(d) <= set(s.ascii_letters + "!." + s.whitespace + s.digits):
            print(k0, k1, k2)
            print(d)

text = [line for line in open('p059_cipher.txt')]
message = text[0].split(',')

foundCipherKey(message[:51])
print(decript2(message, "exp"))

#------------------------------------------------------------
# Another Solution
#------------------------------------------------------------


from string import printable, ascii_lowercase
from itertools import product


def load_message():
    with open("p059_cipher.txt") as f:
        return list(map(int, f.readline().split(",")))


def decipher(t, k):
    msg = []
    for i, c in enumerate(t):
        msg.append(c ^ k[i % len(k)])
    return msg


text = load_message()
allowed = [ord(c) for c in printable]
potential_letters = ({ord(c) for c in ascii_lowercase if all([ord(c) ^ i in allowed for i in text[j::3]])} for j in range(3))

for i in product(*potential_letters):
    string = "".join(map(chr, decipher(text, i)))
    if "euler" in string.lower():
        print(sum(decipher(text, i)))
