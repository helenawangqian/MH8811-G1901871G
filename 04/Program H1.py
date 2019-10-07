#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_min(lst):
    smallest_so_far = None
    for the_num in lst:
        if smallest_so_far is None:
            smallest_so_far = the_num
        if the_num < smallest_so_far:
            smallest_so_far = the_num
    return (smallest_so_far)


# In[2]:


def my_max(lst):
    biggest_so_far = None
    for the_num in lst:
        if biggest_so_far is None:
            biggest_so_far = the_num
        if the_num > biggest_so_far:
            biggest_so_far = the_num
    return (biggest_so_far)


# In[3]:


def my_average(lst):
    count = 0
    sum = 0
    for the_num in lst:
        count = count + 1
        sum = sum + the_num
        avg = sum / count
    return (avg)


# In[4]:


def my_median(lst):
    lst.sort()
    r=int(len(lst)/2)
    if len(lst)% 2 == 0 :
        return (lst[r])
    else:
        return ((lst[r]+lst[r+1])/2) 


# In[5]:


def my_range(lst):
    biggest_so_far = None
    smallest_so_far = None
    for the_num in lst:
        if biggest_so_far is None:
            biggest_so_far = the_num
        if smallest_so_far is None:
            smallest_so_far = the_num
        if the_num > biggest_so_far:
            biggest_so_far = the_num
        if the_num < smallest_so_far:
            smallest_so_far = the_num
    return (biggest_so_far-smallest_so_far)


# In[6]:


def my_samplevariance(lst):
    count = 0
    sum = 0
    m = 0
    for the_num in lst:
        count = count + 1
        sum = sum + the_num
        avg = sum / count
    
    for the_num in lst:
        n = len(lst)
        m = m + (the_num - avg)**2
        samplevariance = m / (n-1)
    return (samplevariance)


# In[7]:


from pathlib import Path

data_folder = Path("/Users/viceva/Downloads/python")

file_to_open = data_folder / "MH8811-04-Data.csv"

def getFileLines(file_to_open):
    fhandle = open(file_to_open)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    return lines


# In[8]:


lst = list(getFileLines(file_to_open))
for i in range(len(lst)):
    lst[i]=int(lst[i])

print('The minimum of the list is ', my_min(lst))
print('The maximum of the list is ', my_max(lst))
print('The average of the list is ',my_average(lst))
print('The median of the list is ',my_median(lst))
print('The range of the list is ',my_range(lst))
print('The samplevariance of the list is ',my_samplevariance(lst))


# In[ ]:




