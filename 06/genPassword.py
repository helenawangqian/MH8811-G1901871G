#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def genPassword(n):
    upper_char = [chr(i) for i in range(65,91)]
    lower_char = [chr(i) for i in range(97,123)]
    num = [chr(i) for i in range(48,58)]
    symbols = [chr(i) for i in range(33,48)]
    
    num1 = random.randint(1,n-3)
    num2 = random.randint(1,n-2-num1)
    num3 = random.randint(1,n-1-num1-num2)
    num4 = n - num1 - num2 - num3
    
    string = ''.join([random.choice(upper_char) for i in range(num1)])
    string += ''.join([random.choice(lower_char) for i in range(num2)])
    string += ''.join([random.choice(num) for i in range(num3)]) 
    string += ''.join([random.choice(symbols) for i in range(num4)])
    
    result = []
    order_list= list(string)
    for i in range(n):
        choice = random.randint(0,n-i-1)
        result.append(order_list.pop(choice))
    return ''.join(result)


if __name__ == " __main__":
    print(genPassword(12))


# In[ ]:




