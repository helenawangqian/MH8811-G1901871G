#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import genPassword

if __name__== '__main__' :        
    n=int(input('What is the password length?'))
    if n < 4:
        print('Error!')
    else:
        print("The password is " + genPassword(n))

