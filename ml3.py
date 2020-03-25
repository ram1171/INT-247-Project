# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:24:46 2019

@author: Ram Teja Chowdary
"""

'''import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10,1)
y=2*x+3
plt.plot(x,y,lw=3,c='g')
plt.xlabel('x-->')
plt.ylabel('y-->')
y=(-2*x)
plt.plot(x,y,lw=3,c='r')
y=4*x+10
plt.plot(x,y,lw=3,c='b')
plt.axhline(c='k')
plt.axvline(c='k')
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10,1)
y=2*x+3
plt.plot(x,y,lw=3,c='g')
plt.xlabel('x-->')
plt.ylabel('y-->')
y=(-2*x)
plt.plot(x,y,lw=3,c='r')
y=4*x+10
plt.plot(x,y,lw=3,c='b')
y2=np.zeros(x.shape)
plt.plot(x,y2,c='k')
plt.plot(y2,x,c='k')
plt.show()