#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Program 01: Output 'Hello, World!'
def p01():
    print("\n"+'Hello,World!'+ "\n")

#Program 02-1: Output personalized 'Hello,World!'
def p02_1():
    nam = input ('Who are you?')
    print("\n"+'Hello,',nam,'!'+ "\n")
    
#Program 02-2: Celsius to Fahrenheit Converter
def p02_2():
    str_input = input ('What is the degree in Celsius?')
    C = float (str_input)
    print("\n"+'The corresponding degree in Fahrenheit is:', C*1.8+32)
    print("\n")
    
    
# main menu for user to choose
def menu():
    print('------------------------------------')
    print('Sub-Programs available for choosing:')
    print('Program 01:Output Hello, World!')
    print('Program 02-1:Output personalized Hello,World!')
    print('Program 02-2:Celsius to Fahrenheit Converter ')
    print('------------------------------------')
    
while True:
    menu()
    choice = input ('Your choice, press Q to exit:')
    if choice == '01':
        p01()
    elif choice == '02-1':
        p02_1()
    elif choice == '02-2':
        p02_2()
    elif choice == 'Q':
        break
    else: 
        print("\n"+'Please type in the exact number of the program!!'+"\n")
        
print("\n")
print("\n")
print("\n")
print('Thank you for using the program!')
        
        


# In[ ]:




