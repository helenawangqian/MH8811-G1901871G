#!/usr/bin/env python
# coding: utf-8

# In[26]:


#input integers
ddd=dict()
i=0
while True:
    i=i+1
    key =input('Enter key %d, press enter twice if you are done inputting: '%i)
    value = input('Enter value %d, press enter twice if you are done inputting: '%i)
    if key=='':
        break
    ddd[key] = value
print(ddd)


# In[27]:


#defining serialize and deserialize
def serialize(l):
    res = ''
    for key in l:
        res = res+ key + ',' + str(l[key])
        res = res + '|'
    return res[:-1]

def deserialize(s):
    dict_of_str = s.split('|')
    res = dict()
    for string in dict_of_str:
        a = string.split(',')[0]
        b = string.split(',')[1]
        res[a]=b
    return res


# In[28]:


#input lst from user
if ddd is '':
    serialized = ''
else:
    serialized = serialize(ddd)
print('The serialized dictionary is:', serialized)


# In[29]:


#write to file
import json
filename = input ('What would you want to file name to be? ')
f = open(filename, 'w')
json.dump(serialized, f)
f.close()

print('The file has been saved')


# In[34]:


#read from file
import json
from pprint import pprint

with open(filename) as json_data:
    d = json.load(json_data)
    json_data.close()
if d is '':
    dict2 = {}
else:
    dict2 = deserialize(d)


print(dict2)


# In[35]:


#compare the lists
if ddd == dict2: 
    print ("Success!") 
else : 
    print ("Fail!")


# In[ ]:




