#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:52:02 2019
FUNCTIONS
@author: abiram
"""
def itsfun():       #Unlike C function must be defined before the declaration
    print("This is a function statement.")
    
itsfun()            #Function declaration

def funum(a,b):     #Passing values inside the functions
    print(a,b)
    c=a+b
    d=a-b
    return c,d      #Returning of values

ret1,ret2 = funum(6,5)  #Should define amount of return values to variable aswell, here 2 values are returning
print(ret1, ret2)       #so 2 variables are used.

#OUTPUT:
#This is a function statement.
#6 5
#11 1