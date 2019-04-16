#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:10:37 2019
More on variables
@author: abiram
"""

a=25    #Assigning a value to the variable
print(id(a))    #printing the memory location of the variable
b=a         #Assigning the value of var a to var b
print(id(b))    #printing the memory location of the variable b which has the same memory location
print(id(25)) #Eventhough the id of value also point to the same location, here the value is called an object
a=87    #Changing the value of a to 87
print(id(a))    #Instead of earasing the old value, the value is saving into new memory location.
b=a     #Assigning the new value of a to b
print(id(b))    #New memory location will get printed
c=65
print(id(c))    
print(id(25)) #Now the old value(object) will become a garbage value

print(type(a))   #printing the type of a variable
name="ABIRAM"   
print(type(name))
PI=3.14
print(type(PI))

#NOTE: THERE IS NO CONSTANT IN PYTHON.!


#Output
#8830464
#8830464
#8830464
#8832448
#8832448
#8831744
#8830464

#<class 'int'>
#<class 'str'>
#<class 'float'>
