#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:59:31 2019

@author: abiram
"""

val = [10,25,68,54,321] #List example, no need to specify the integer type
print(val)
print(val[2:])
print(val[:-1]) #minus values can also be applicable
str = ["starscream","optimus","bee"] #can also be in a string format
print(str)
print(str)
misc = [2.67,"Abiram",35] #also can be in a mixed types
print(misc)
print(val, misc, val)




#Output
#[10, 25, 68, 54, 321]
#[68, 54, 321]
#[10, 25, 68, 54]
#['starscream', 'optimus', 'bee']
#['starscream', 'optimus', 'bee']
#[2.67, 'Abiram', 35]
#[10, 25, 68, 54, 321] [2.67, 'Abiram', 35] [10, 25, 68, 54, 321]
