# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:59:30 2018

@author: Dinesh
"""
from cryptography.fernet import Fernet
    
def fun(x1):  
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)
  text=x1
  encoded_text = cipher_suite.encrypt(text.encode(encoding='utf-8'))
  decoded_text = cipher_suite.decrypt(encoded_text)
  return encoded_text.decode("utf-8") ,key.decode("utf-8")