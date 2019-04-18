#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:13:45 2019
if-elif-else-nestedif
@author: abiram
"""
A=int(input("enter value of A: "))
B=int(input("enter value of B: "))
if A>=B:
    print("A is greater than B.")
    if A<5:
        print("and less than 5")
    elif A==5:
        print("A is equal to 5")
    else:
        print("a is 5")
elif B>=A:
    print("B is greater than A.")
    if B<=5:
        print("and less than 5")
    else:
        print("greater than 5")
else:
    print("Both are equal.")