# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:13:52 2019

@author: Ram Teja Chowdary
"""
import math
import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(-10,10,100)# create 100 points in between -10 to 10
#x=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y=x # linear
plt.figure(1)
plt.subplot(221)
plt.plot(x,y)
plt.title("Linear Activation Function")
plt.xlabel("x")
plt.ylabel("y")

# threshold at Zero
plt.subplot(222)
y=[]
i=0;
while(i<len(x)):
    if x[i]<0:
        y.append(0)
    else:
        y.append(1)
    i+=1
         
plt.plot(x,y)
plt.title("Threshold Function at 0")
plt.xlabel("x")
plt.ylabel("y")
# ramp function
plt.subplot(223)
y=[]
i=0;
while(i<len(x)):
    if x[i]<0:
        y.append(0)
    elif x[i]>1:
        y.append(1)
    else:
        y.append(x[i])
    i+=1
         
plt.plot(x,y)
plt.title("Ramp Function threshold at 1")
plt.xlabel("x")
plt.ylabel("y")

# Log Sigmoid
plt.subplot(224)
y=[]
i=0;
while(i<len(x)):
    y.append(1/(1+math.exp(-x[i])))
    i+=1
         
plt.plot(x,y)
plt.title("Logsigmoid Function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

