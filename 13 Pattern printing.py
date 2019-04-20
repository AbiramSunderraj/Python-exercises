#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:44:31 2019
Pattern printing
@author: abiram
"""

a=input("Enter a Character to print the pattern: ")

i=1
while i<=4:     #Telling number of times the pattern should be repete
    j=1
    while j<=4: #Telling number of times a character should be repete
        print(a  , " ", end="")
        j+=1
    i+=1
    print("")
    

#OUTPUT
#Enter a Character to print the pattern: $
#$  $  $  $  
#$  $  $  $  
#$  $  $  $  
#$  $  $  $   
    
a=input("Enter a Character to print the pattern: ")

i=1
while i<=4:     #Telling number of times the pattern should be repete
    j=0+i
    while j<=4: #Telling number of times a character should be repete
        print(a  , " ", end="")
        j+=1
    i+=1
    print("")

#OUTPUT
#Enter a Character to print the pattern: *
#*  *  *  *  
#*  *  *  
#*  *
#*

a=input("Enter a Character to print the pattern: ")

i=1
while i<=4:     #Telling number of times the pattern should be repete
    j=1
    while j<=i: #Telling number of times a character should be repete
        print(a  , " ", end="")
        j+=1
    i+=1
    print("")

#OUTPUT
#Enter a Character to print the pattern: %
#%  
#%  %  
#%  %  %  
#%  %  %  %  