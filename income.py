# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:47:03 2019

@author: Shrutika
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Clustering\income.csv')
df.columns
x=pd.DataFrame(df.Age)
y=pd.DataFrame(df.Income)
d=dendrogram(linkage(x,method='ward'))
from sklearn.cluster import AgglomerativeClustering
obj=AgglomerativeClustering(n_clusters=2)
obj.fit_predict(x)
plt.figure(figsize=(15,7))
plt.scatter(x.Age,y.Income,c=obj.labels_,cmap='rainbow')
