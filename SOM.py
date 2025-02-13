# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:53:30 2019

@author: Ram Teja Chowdary
"""

import numpy as np
x = np.array([[ 1, 1, 0, 0],[0, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1]])
w =np.array([[0.2 ,0.8], [0.6, 0.4], [0.5, 0.7], [0.9, 0.3]])
lrate= 0.6
e=1
D=[0,0]
print('learning rate of this epoch is',lrate);
while(e<=3): # e is epoch
    print('Epoch is',e);
    
    for i in range(4): # number of patterns 4
        for j in range(2): # size of neurons 
             temp=0
             for k in range(4):
                temp = temp + ((w[k,j]-x[i,k])**2)
             D[j]=temp # distance matrix
        #decide winner neurons
        if(D[0]<D[1]):
            J=0
        else:
            J=1
        print('winning unit is',J+1)
        print('weight updation ...')
        for m in range(4):
             w[m,J]=w[m,J] + (lrate *(x[i,m]-w[m,J]))
        print('Updated weights',w)
        

    e=e+1
    lrate = 0.5*lrate;
    print(' updated learning rate after ',e,' epoch is',lrate)