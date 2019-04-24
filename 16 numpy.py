#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:31:30 2019
numpy
@author: abiram
"""

from numpy import *  #importing everything from numpy module

arr1 = array([1,2,3,4,5]) #Array data types is optional
print("arr =", arr1)

lin = linspace(1,20,5)   #Array will be equally divided into 5 seperations inbetween 1 to 20. Default type is float.
print("Lin =", lin)

log = logspace(1,20)    #Array will be equally divided based on log i.e. 10*1 to 10^20. For both lin and log default seperation value is 50.
print("Log =", log)

ar = arange(1,10)   #aRange in array
print("ar =",ar)

zer = zeros(5)      #print only zeros for specfied number of times, default is float data type.
print("zeros =", zer)

one = ones(4, int)  #print only ones for specfied number of times in int format
print("Ones =", one)



#OUTPUT
#arr = [1 2 3 4 5]
#Lin = [ 1.    5.75 10.5  15.25 20.  ]
#Log = [1.00000000e+01 2.44205309e+01 5.96362332e+01 1.45634848e+02
# 3.55648031e+02 8.68511374e+02 2.12095089e+03 5.17947468e+03
# 1.26485522e+04 3.08884360e+04 7.54312006e+04 1.84206997e+05
# 4.49843267e+05 1.09854114e+06 2.68269580e+06 6.55128557e+06
# 1.59985872e+07 3.90693994e+07 9.54095476e+07 2.32995181e+08
# 5.68986603e+08 1.38949549e+09 3.39322177e+09 8.28642773e+09
# 2.02358965e+10 4.94171336e+10 1.20679264e+11 2.94705170e+11
# 7.19685673e+11 1.75751062e+12 4.29193426e+12 1.04811313e+13
# 2.55954792e+13 6.25055193e+13 1.52641797e+14 3.72759372e+14
# 9.10298178e+14 2.22299648e+15 5.42867544e+15 1.32571137e+16
# 3.23745754e+16 7.90604321e+16 1.93069773e+17 4.71486636e+17
# 1.15139540e+18 2.81176870e+18 6.86648845e+18 1.67683294e+19
# 4.09491506e+19 1.00000000e+20]
#ar = [1 2 3 4 5 6 7 8 9]
#zeros = [0. 0. 0. 0. 0.]
#Ones = [1 1 1 1]