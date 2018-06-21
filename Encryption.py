# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:59:43 2018

@author: Dinesh
"""
import string as s
import random as r
passwd=r.sample(s.ascii_letters + s.digits, 62)
passwd="".join(passwd)
print(passwd.encode(encoding='utf-8'))

text = s.ascii_letters + s.digits
text=text.encode(encoding='utf-8')
key = passwd.encode(encoding='utf-8')

print(passwd)

enc_table = bytes.maketrans(text, key)
dec_table = bytes.maketrans(key, text)


result = ''
choice = ''
message = ''

while choice != '0':
    choice = input("\n Do you want to encrypt or decrypt the message?\n 1 to encrypt, 2 to decrypt or 0 to exit program. ")

    if choice == '1':
        message = input('\nEnter message for encryption: ')
        result = message.translate(enc_table)
        print(result + '\n')

    elif choice == '2':
        message = input('\nEnter message to decrypt: ')
        result = message.translate(dec_table)
        print(result + '\n')

    elif choice != '0':
        print('You have entered an invalid input, please try again. \n\n')

print("Working")