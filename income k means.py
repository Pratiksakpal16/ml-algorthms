# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:13:37 2019

@author: Shrutika
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Clustering\income.csv')
df.columns

x=pd.DataFrame(df.Age)
y=pd.DataFrame(df.Income)
from sklearn.cluster import KMeans
obj=KMeans(n_clusters=4)
obj.fit_predict(x)
b=obj.cluster_centers_
plt.scatter(x.Age,y.Income,c=obj.labels_,cmap='rainbow')
plt.scatter(b[:,0],b[:,1],marker='*',s=60,color='red')
