# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:07:55 2019

@author: Shrutika
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\New folder\wine.csv')
dt.columns
type=np.sum(dt['Type'])
alcohol=np.sum(dt['Alcohol'])
malic=np.sum(dt[ 'Malic'])
ash=np.sum(dt['Ash'])
alcalinity=np.sum(dt['Alcalinity'])
magnesium=np.sum(dt['Magnesium'])
phenols=np.sum(dt['Phenols'])
flavanoids=np.sum(dt['Flavanoids'])
nonflavanoids=np.sum(dt['Nonflavanoids'])
proanthocyanins=np.sum(dt['Proanthocyanins'])
color=np.sum(dt['Color'])
hue=np.sum(dt['Hue'])
dilution=np.sum(dt['Dilution'])
li=[alcohol,malic,ash,alcalinity,magnesium,phenols,flavanoids,nonflavanoids,proanthocyanins,color,hue,dilution]
print('list',li)
x=pd.DataFrame(dt.Alcohol)
x['Malic']=dt.malic
x['Ash']=dt.ash
x['Alcalinity']=dt.alcalinity
x['Magnesium']=dt.magnesium
x['Phenols']=dt.phenols
x['Flavanoids']=dt.flavanoids
x['Nonflavanoids']=dt.nonflavanoids
x['Proanthocyanins']=dt.proanthocyanins
x['Color']=dt.color
x['Hue']=dt.hue
x['Dilution']=dt.dilution
x=df.drop('Type',axis=1)
y=df.Type
plt.figure(figsize=(10,10))
plt.pie(li,labels=x,autopct='%2.2f%%',radius=1.0)
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
acc1=accuracy_score(y,pr1)
from sklearn.neighbors import KNeighborsClassifier
obj=KNeighborsClassifier(n_clusters=8)
pr2=obj.fit_predict(x)
ab=obj.cluster_centers_
from sklearn.metrics import accuracy_score
acc2=accuracy_score(y,pr2)
from sklearn.tree import DecisionTreeClassifier
obj=DecisionTreeClassifier()
obj.fit(x,y)
pr3=obj.predict(x)
from sklearn.metrics import accuracy_score
acc3=accuracy_score(y,pr3)
from sklearn.ensemble import RandomForestClassifier
obj=RandomForestClassifier()
obj.fit(x,y)
pr4=obj.predict(x)
from sklearn.metrics import accuracy_score
acc4=accuracy_score(y,pr4)