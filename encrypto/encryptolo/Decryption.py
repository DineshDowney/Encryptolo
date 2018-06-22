# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:59:30 2018

@author: Dinesh
"""
import sys
import os

# args=sys.argv
# if len(args)!=3:
#   print ("\nError !!! Wrong number of parameters")
#   print ("\nUsages: $python encrypt.py <Text> <Key>")
#   print ("\nExample: $python encrypt.py text_to_be_encrypted \n")
#   exit()

# text,key=args[1],args[2]

from cryptography.fernet import Fernet
    
def fun(text,key):
    cipher_suite = Fernet(key)
    #encoded_text = cipher_suite.encrypt(text.encode(encoding='utf-8'))
    decoded_text = cipher_suite.decrypt(text.encode(encoding='utf-8'))
    print(decoded_text.decode("utf-8"))
    return decoded_text.decode("utf-8")
    

#print(decoded_text.decode("utf-8"))
#x=decoded_text.decode("utf-8")