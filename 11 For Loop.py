#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:54:57 2019
FOR loop
@author: abiram
"""

#For loop is used when manipulating lists, ranges, strings, etc...

i=['Sansa', 'Arya', 'Bran']  #LISTS
for a in i:
    print(a)

j={1,2,3,4,5}               #SETS
for b in j:
    print(b," ", end="")
    
print()

k = range(1,26,1)           #RANGES
for c in k:
    if c%5==0:
        print(c," ", end="")
        
print()                     #STRINGS
for d in "DRACARYS":
    print(d, " ", end="")
    
    
#OUTPUT
#Sansa
#Arya
#Bran
#1  2  3  4  5  
#5  10  15  20  25  
#D  R  A  C  A  R  Y  S  