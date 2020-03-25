# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:15:07 2019

@author: Ram Teja Chowdary
"""

#Plot y=x^2
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,11,1)
y=x**2
plt.plot(x,y,lw=3,ls='--',c='g',marker='s',markersize=10,markerfacecolor='r',markeredgecolor='k')
plt.legend(['y=X**2'])
plt.title('y=X^2')
plt.xlabel('x-->')
plt.ylabel('y-->')
plt.show()