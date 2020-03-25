# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:23:54 2019

@author: Ram Teja Chowdary
"""

l=[]
for i in range(2,21,2):
    l.append(i)
print(l)

import pandas as pd
k=pd.read_csv('Book1.csv',header=None)
print('Read succesfully')
k.columns=['A','B','C','D','E']
print(k)
print(k.head()) #display first 5 rows
print(k.tail()) #dislay last 5 rows
print(k.describe()) #used to describe the data
print(k.columns)
print(k['A'])
print(k.iloc[0])
###
import numpy as np
data=np.array(k)
print(data)
print(data.shape)
print(data.size)
print(data[1,:])
##
x=[0,0,0,0,0,1,1,1,0,1]
p=np.array(x)
print(np.unique(p))
print(np.sum(p==0))
print(np.sum(p==1))


