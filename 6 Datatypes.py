#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:32:50 2019
Datatypes
@author: abiram
"""

#1. NONE - when there is no value for a variable

#2. NUMERIC - 4 types
#2.a Integer
a=4

#2.b Float
b=3.5

#2.c Complex (a+bj)
c=complex(a,b)
print(c)

#2.d Bool
print(a<b)

#3. List
lst=[24,35,25,15,14]

#4. Tuple
tup=(24,35,25,15,14)

#5. Set
sets={24,35,25,15,14}

#6. String
string="ABIRAM SUNDARRAJ"

#7. Range
Range=range(0,5)
print(list(Range))

#8. Dictionary - used to store/map a value to anything, dictionary key must be unique. Whatever value can be stored.

dictionary={"abi":'9876543210',"aks":"9876543211","dhars":"9876543212"}
print(dictionary)
key=dictionary.keys() #Fetch keys with the help of inbuilt Keys() function
value=dictionary.values() #Fetch Values with the help of inbuilt values() function
print(key)
print(value)
keyofabi=dictionary.get("abi")
print(keyofabi)


#OUTPUT:
#(4+3.5j)
#False
#[0, 1, 2, 3, 4]
#{'abi': '9876543210', 'aks': '9876543211', 'dhars': '9876543212'}
#dict_keys(['abi', 'aks', 'dhars'])
#dict_values(['9876543210', '9876543211', '9876543212'])
#9876543210
