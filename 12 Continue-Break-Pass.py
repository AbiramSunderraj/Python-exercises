#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:30:48 2019
Continue-Break-Pass
@author: abiram
"""

i=range(1,5)

for a in i:
    if a==3:
        continue    #Used to skip the specfic condition
    print(a, " ", end="")
    
print()

for a in i:
    if a==3:
        break      #Used to exit out of the loop when the control reaches
    print(a, " ", end="")
    
print()

for a in i:
    if a%2==0:
        pass        #used  to skip the block or function or  thing when the programmer is not confirmed in its working part
    else:
        print(a, " ", end="")


#OUTPUT
#1  2  4  
#1  2  
#1  3  