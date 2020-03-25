# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 08:50:02 2019

@author: Ram Teja Chowdary
"""

import numpy as np
X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([-1,1,1,1])
class Perceptron:
    def __init__(self,lr,n):
        self.lr=lr
        self.n=n
    def fit(self,X,y):
        self.w=np.zeros(1+X.shape[1])
        for _ in range(self.n):
            for xi,target in zip(X,y):
                error=target-self.predict(xi)
                if error!=0:
                    update=self.lr*error
                    self.w[0]+=update*1
                    self.w[1:]+=update*xi
        return self
    def netinput(self,X):
        return np.dot(X,self.w[1:])+self.w[0]
    def predict(self,X):
        return np.where(self.netinput(X)>=0,1,-1)
ppn=Perceptron(0.1,10)
ppn.fit(X,y)
print('o/p for [1,1]=',ppn.predict([1,1]))
print('o/p for [0,0]=',ppn.predict([0,0]))
print('weights',ppn.w)
        