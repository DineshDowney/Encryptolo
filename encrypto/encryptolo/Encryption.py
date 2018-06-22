# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:59:30 2018

@author: Dinesh
"""
import sys
import os

args=sys.argv
if len(args)!=2:
  print ("\nError !!! Wrong number of parameters")
  print ("\nUsages: $python encrypt.py <Text>")
  print ("\nExample: $python encrypt.py text_to_be_encrypted \n")
  exit()


from cryptography.fernet import Fernet
    
def fun(x1):  
  key = Fernet.generate_key() #this is your "password"
  cipher_suite = Fernet(key)
  text=x1
  encoded_text = cipher_suite.encrypt(text.encode(encoding='utf-8'))
  decoded_text = cipher_suite.decrypt(encoded_text)
  return encoded_text.decode("utf-8") ,key.decode("utf-8")

#print(encoded_text.decode("utf-8") ,key.decode("utf-8") )
#x=encoded_text.decode("utf-8")
#y=key.decode("utf-8")