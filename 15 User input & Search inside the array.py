#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:53:58 2019
Array, getting input from user and search for index number.
@author: abiram
"""
from array import *

values = array('i', [])

x = int(input("Enter the size of an array: "))

for i in range(x):
    a=int(input("Enter value: "))
    values.append(a)

print(values)

k = int(input("Enter the value to find index number: "))
print("Index of", k, "is: ", values.index(k))