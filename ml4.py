# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:41:48 2019

@author: Ram Teja Chowdary
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,11,1)
y1=2*x+3
y2=-2*x
y3=4*x+10
y4=np.sin(x)
plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title('y=2*x+3')
plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title('y=-2*x')
plt.subplot(2,2,3)
plt.plot(x,y3)
plt.title('y=4*x+10')
plt.subplot(2,2,4)
plt.plot(x,y4)
plt.title('y=sinx')