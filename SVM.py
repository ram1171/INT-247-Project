# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:52:10 2019

@author: Ram Teja Chowdary
"""

from sklearn import datasets
import numpy as np
iris=datasets.load_iris()
X=iris.data
y=iris.target
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.3,random_state=0)
from sklearn.svm import SVC
svm = SVC(kernel='linear', C=1, random_state=0)
svm.fit(X_train, y_train)
y_pred=svm.predict(X_test)
print('misclassified samples: %d'%(y_test!=y_pred).sum())#compute
from sklearn.metrics import accuracy_score
print('Accuracy:%.2f'%accuracy_score(y_test,y_pred))