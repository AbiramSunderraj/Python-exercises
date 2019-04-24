#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:43:58 2019
Copying an array
@author: abiram
"""
from numpy import *                 #Importing numpy

arr1=array([12,13,15,2,8])          
arr2=array([1,2,3,3,4])

print(concatenate([arr1,arr2]))     #concat both arrays
print(sin(arr1))                    #performing sin function
print(cos(arr2))                    #performing cos function
print(sum(arr1))                    #sum of an array
arr = arr1 + 5                      #adding 5 to each element in an array
print(arr)

array = arr1                        #copying an array, its just maps 'array' to arr1 address
print(array)
print("arr1 id =",id(arr1), ",", "arr id =", id(arr))

#SHALLOW COPY
arr3 = arr2.view()                  #view function is used to copy an array in a different location
print(arr3)
print("arr2 id =",id(arr2), ",", "arr3 id =", id(arr3))
arr2[2] = 6                         #whatever change we make is, it will be reflected on another one too
print(arr2, arr3)
print("arr2 id =",id(arr2), ",", "arr3 id =", id(arr3))

#DEEP COPY5
arr4 = arr2.copy()                  #view function is used to copy an array in a different location
print(arr4)
print("arr2 id =",id(arr2), ",", "arr4 id =", id(arr4))
arr4[2] = 5                         #whatever change we make is, it will not reflect on another one too
print(arr2, arr4)
print("arr2 id =",id(arr2), ",", "arr4 id =", id(arr4))

#OUTPUT
#[12 13 15  2  8  1  2  3  3  4]
#[-0.53657292  0.42016704  0.65028784  0.90929743  0.98935825]
#[ 0.54030231 -0.41614684 -0.9899925  -0.9899925  -0.65364362]
#50
#[17 18 20  7 13]
#[12 13 15  2  8]
#arr1 id = 140624765923536 , arr id = 140624765923856
#[1 2 3 3 4]
#arr2 id = 140624765923616 , arr3 id = 140624765923696
#[1 2 6 3 4] [1 2 6 3 4]
#arr2 id = 140624765923616 , arr3 id = 140624765923696
#[1 2 6 3 4]
#arr2 id = 140624765923616 , arr4 id = 140624765924176
#[1 2 6 3 4] [1 2 5 3 4]
#arr2 id = 140624765923616 , arr4 id = 140624765924176