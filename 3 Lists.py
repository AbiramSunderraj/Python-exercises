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

#using some inbuilt functions
val.append(87) #Appending 87 at the end of list
print(val) 
val.insert(3,666) #Inserting values at the 3rd index position
print(val)
val.extend([25,35,45]) #Extending the list
print(val)
val.pop() #Used to remove an element, in this case it will remove the last element
print(val)
val.pop(1) #removes 1st element
print(val)
val.sort() #Sorting from min to max
print(val)
mini = min(val) #Getting minimum value
maxi = max(val) #Getting maximum value
print(mini, maxi)




#Output
#[10, 25, 68, 54, 321]
#[68, 54, 321]
#[10, 25, 68, 54]
#['starscream', 'optimus', 'bee']
#['starscream', 'optimus', 'bee']
#[2.67, 'Abiram', 35]
#[10, 25, 68, 54, 321] [2.67, 'Abiram', 35] [10, 25, 68, 54, 321]
#[10, 25, 68, 54, 321, 87]
#[10, 25, 68, 666, 54, 321, 87]
#[10, 25, 68, 666, 54, 321, 87, 25, 35, 45]
#[10, 25, 68, 666, 54, 321, 87, 25, 35]
#[10, 68, 666, 54, 321, 87, 25, 35]
#[10, 25, 35, 54, 68, 87, 321, 666]
#10 666
