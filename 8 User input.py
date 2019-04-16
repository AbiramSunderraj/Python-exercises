#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:55:02 2019
User Input
@author: abiram
"""
import sys

a=int(input("Enter a value a: "))
b=int(input("Enter a value b: "))
print("Output is " , a+b) 
print("Output is " + str(a+b)[0]) #Showing output by the specified index.

c=int(input("Enter a value c: ")[0]) #Getting input by the specified index
d=int(input("Enter a value d: ")[1])
print("Output is " + str(c+d)[1]) 
print("Output is ", c+d)


#The below code will be used while using terminal execution and take the arguments as inputs then and there itself. Should be import sys function.
#x=int(sys.argv[1])  #will be the filename, so 1 is taken
#y=int(sys.argv[2])
#print(x+y)

#OUTPUT
#Enter a value a: 25

#Enter a value b: 25
#Output is  50
#Output is 5

#Enter a value c: 87

#Enter a value d: 78
#Output is 6
#Output is  16
