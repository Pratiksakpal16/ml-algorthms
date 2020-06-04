# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:05:37 2019

@author: Shrutika
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\EDA-Datasets\drinks.csv')
dt.columns
beer=np.sum(dt['beer_servings'])
spirit=np.sum(dt['spirit_servings'])
wine=np.sum(dt[ 'wine_servings'])
total=np.sum(dt['total_litres_of_pure_alcohol'])
li=[beer,spirit,wine]
print('list',li)
x=('beer','spirit','wine')
x=pd.DataFrame('beer','spirit','wine')
y=pd.DataFrame('total')
plt.figure(figsize=(10,10))
plt.pie(li,labels=x,autopct='%2.2f%%',radius=1.0)
plt.title('Drinks')
from sklearn.naivebayes import GaussianMB
obj=GaussianMB()
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,pr)
from sklearn.svm import LinearSVC
obj=LinearSVC()
obj.fit(x,y)
pr1=obj.predict(x)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,pr1)
from sklearn.neighbors import KNeighborsClassifier
obj=KNeighborsClassifier(n_clusters=8)
pr2=obj.fit_predict(x)
ab=obj.cluster_centers_
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,pr2)
from sklearn.tree import DecisionTreeClassifier
obj=DecisionTreeClassifier()
obj.fit(x,y)
pr3=obj.predict(x)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,pr3)