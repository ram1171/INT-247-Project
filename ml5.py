# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:54:46 2019

@author: Ram Teja Chowdary
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(10,-10,-0.5)
y=x
def threshold(x):
    if x>=0:
        return x
    else:
        return 0
threshold=np.vectorize(threshold)
y1=threshold(x)
def ramp(x):
    if x>1:
        return 1
    elif 1<=x and x>=0:
        return x
    else:
        return 0
ramp=np.vectorize(ramp)
y2=ramp(x)
y3=1/(1+np.exp(-x))
plt.subplot(2,2,1)
plt.title("Linear")
plt.plot(x,y)
plt.subplot(2,2,2)
plt.title("Threshold at 0")
plt.plot(x,y1)
plt.subplot(2,2,3)
plt.title("Ramp")
plt.plot(x,y2)
plt.subplot(2,2,4)
plt.title("Log-Sigmoid")
plt.plot(x,y3)
plt.show()

