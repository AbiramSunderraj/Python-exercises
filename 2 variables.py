"""
Created on Sat Apr 13 23:47:00 2019

@author: abiram
"""

x = 3 #assign 3 for variable x
y = 7 #assign 7 for variable y
print(x)
print(y)
print("x+y") #string function
print(x+y) #integer function
X=10    #variable name is case sensitive
print(X+y)

var="ANACONDA" #Assigning string value to the variable, acts like an array
print(var)
print(var[0]) #Used to access a single character in an array
print(var[0:])
print(var[:10])
print(var[0:3])
print(var[1:6])
print(var[-2]) #print from reverse i.e. from last variable will be considered as -1, -2, -3 and so on...
print(var[-5:-1])
print("This code is executed using " + var + " IDE.")
print(len(var)) #can able to find length of the string using inbuilt len() function.



#OUTPUT
#3
#7
#x+y
#10
#17
#ANACONDA
#A
#ANACONDA
#ANACONDA
#ANA
#NACON
#D
#COND
#This code is executed using ANACONDA IDE.
#8
