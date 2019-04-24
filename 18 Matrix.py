#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:56:19 2019
MATRIX
@author: abiram
"""
from numpy import *

m = array([         #Matrix format
      
      [2,3,6],
      [1,7,5]
      
      ])
print("Type of matrix =", m.ndim)   #will show the dimnession of matrices
print("Shape is:", m.shape)         #display the matrix as its shape
mat = m.flatten()                   #Flatten the matrices
print(mat)

#2 DIMENSIONAL ARRAY
m1 = array([
        [1,2,3,4,5,6,7,8,9,10,11,12]
        ])
rshp = m1.reshape(4,3)              #reshope into 3-D format
print(rshp)
print("")

#3 DIMENSIONAL ARRAY
m2 = array([
        [1,2,3,4,5,6,7,8,9,10,11,12]
        ])
rshp = m2.reshape(2,2,3)            #reshope into 3-D format
print(rshp)

print("")
print("Diagonal of m is:", diagonal(m)) #print the diagonal form for the 2 matrices

#MATRIX MULTIPLICATION
m3=([
     [4,5,6],
     [1,2,3]
     ])
print("")
mul = m*m3                          #Multiplication of matrices
print(mul)


#OUTPUT
#Type of matrix = 2
#Shape is: (2, 3)
#[2 3 6 1 7 5]
#
#[[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]
#
#[[[ 1  2  3]
#  [ 4  5  6]]
#
# [[ 7  8  9]
#  [10 11 12]]]
#
#Diagonal of m is: [2 7]
#[[ 8 15 36]
# [ 1 14 15]]

