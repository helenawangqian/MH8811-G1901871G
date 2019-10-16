#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json


def serialize(data):
    res=''
    t=type(data).__name__
    dtype={'list':'1','dict':'2', 'float':'3', 'int':'4', 'str':'5'}
    if dtype[t] == '1':
        for i in data:
            res = res + str(i) + dtype[type(i).__name__] + '|'
    if dtype[t] == '2':
        for key in data:
            res=res+ key + ',' + str(data[key]) + dtype[type(data[key]).__name__] + '|'
    res=res+':'+dtype[t]
    return(res)


def deserialize(data):
    dtype={ '3':'float', '4':'int', '5':'str'}
    t=data.split(':')[1]
    ls_str=(data.split(':')[0]).split('|')[:-1]
    if t=='1':
        ls=[]
        for i in ls_str:
            if i[-1]!='5':
                s=eval(dtype[i[-1]] + '(' + i[:-1] + ')')
            else:
                s=i[:-1]
            ls.append(s)
        return(ls)
    if t=='2':
        d={}
        for i in ls_str:
            a,b=i.split(',')[0],i.split(',')[1]
            if i[-1]!='5':
                d[a]=eval(dtype[b[-1]]+ '(' + b[:-1] + ')')
            else:
                d[a]=b[:-1]
        return(d)
    
    

def read_json_file():
    filename=input('Enter the file name that you want to open: ')
    fh=open(filename)
    data=json.load(fh)
    fh.close()
    print(data)
    return(data)
    



def write_json_file(contents):
    filename=input('Enter the file name that you want to save: ')
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close() 
    return(filename)



def get_file_str():
    filename=input('Please reenter the file name that you want to save')
    fhandle = open(filename)
    lines = ''
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines=lines+line
    fhandle.close()
    return lines






data=read_json_file()
data_str=serialize(data)
filename=save_to_file(data_str)
read_data_str=get_file_str()
des_data=deserialize(read_data_str)
print(des_data)

if data == des_data:
       print('Success!')
else:
       print('Failed!')



# In[ ]:




