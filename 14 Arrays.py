import array as arr      #importing array file

values=arr.array('i', [25,36,64,91]) #initializing array

print(values)       #Printing array
    
for i in values:    #Printing array values using loop
    print(i, " ", end="")
    
values.reverse()    #reverse function in an array

print(values)       #Printing reversed array

for a in range(len(values)):  #Printing array by specify the range
    print(values[a], " ", end="")

print("")
print("Buffer Info:",values.buffer_info())  #To view buffer info i.e. location and size of the array

newarr = arr.array(values.typecode, (j//2 for j in values)) #passing values from one array to another and dividing them by 2

for k in range(len(newarr)):
    print(newarr[k], " ", end="")


#OUTPUT   
#array('i', [25, 36, 64, 91])
#25  36  64  91  array('i', [91, 64, 36, 25])
#91  64  36  25  
#Buffer Info: (140588281031792, 4)
#45  32  18  12 