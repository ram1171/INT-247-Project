# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:02:22 2019

@author: Ram Teja Chowdary
"""
import matplotlib.pyplot as plt
import numpy as np
from ml5 import threshold,ramp
inp=[]
wgt=[]
n=0
for i in range(5):
    x=int(input("Enter Input Vector\n"))
    inp.append(x)
for i in range(5):
    x=int(input("Enter Weight\n"))
    wgt.append(x)
b=int(input("enter bias"))
for i in range (5):
    n=(inp[i]*wgt[i])+n
net=n+b

print('1.Linear')
print('2.Threshold')
print('3.Ramp')
print('4.Log-Sigmoid')
k=int(input("Enter your choice"))
if k==1:
    print("Linear"+str(n))
elif k==2:
    print("threshold"+str(threshold(n)))
elif k==3:
    print("ramp "+str(ramp(n)))
elif k==4:
    print("sigmoid"+str(1/1+np.exp(-n)))
else:
    print("invalid choice")
    
    

