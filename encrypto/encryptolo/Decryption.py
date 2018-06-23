# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:59:30 2018

@author: Dinesh
"""
from cryptography.fernet import Fernet
    
def fun(text,key):
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(text.encode(encoding='utf-8'))
    print(decoded_text.decode("utf-8"))
    return decoded_text.decode("utf-8")