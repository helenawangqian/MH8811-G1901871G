#!/usr/bin/env python
# coding: utf-8

# In[1]:


#input integers
lst=[]
i=0
while True:
    i=i+1
    integer=input('Enter integer %d, press enter again if you are done inputting: '%i)
    if integer=='':
      break
    lst.append(integer)
print(lst)


# In[2]:


#defining serialize and deserialize
def serialize(l):
    res = ''
    for i in l:
        res = res + str(i)
        res = res + '|'
    return res[:-1]

def deserialize(s):
    lst_of_str = s.split('|')
    res = list()
    for string in lst_of_str:
        res.append(string)
    return res


# In[3]:


#input lst from user
if lst is '':
    serialized = ''
else:
    serialized = serialize(lst)
print('The serialized list is:', serialized)


# In[4]:


#write to file
import json
filename = input ('What would you want to file name to be? ')
f = open(filename, 'w')
json.dump(serialized, f)
f.close()

print('The file has been saved')


# In[5]:


#read from file
import json
from pprint import pprint

with open(filename) as json_data:
    d = json.load(json_data)
    json_data.close()
if d is '':
    lst2 = []
else:
    lst2 = deserialize(d)


print(lst2)


# In[6]:


#compare the lists
if lst == lst2: 
    print ("Success!") 
else : 
    print ("Fail")


# In[ ]:




