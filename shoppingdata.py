# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:55:52 2019

@author: Shrutika
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Clustering\shopping_data (1).csv')
df.columns
from sklearn.cluster import KMeans
x=pd.DataFrame(df['Age'])
y=pd.DataFrame(df['Annual Income (k$)'])
obj=KMeans(n_clusters=8)
obj.fit_predict(x)
ab=obj.cluster_centers_
plt.scatter(df['Age'],df['Annual Income (k$)'],c=obj.labels_,cmap='rainbow')
plt.scatter(ab[:,0],ab[:,0],marker='*',s=60,color='red')
