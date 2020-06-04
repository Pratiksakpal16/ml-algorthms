# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:05:34 2019

@author: Shrutika
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Clustering\shopping_data (1).csv')
df.columns
x=pd.DataFrame(df['Age'])
y=pd.DataFrame(df['Annual Income (k$)'])
l=linkage(x,method='ward')
de=l.shape
d=dendrogram(linkage(x,method='ward'))
from sklearn.cluster import AgglomerativeClustering
obj=AgglomerativeClustering(n_clusters=de[1])
obj.fit_predict(x)
plt.figure(figsize=(15,7))
plt.scatter(df'[Age'],df['Annual Income (k$)'],c=obj.labels_,cmap='rainbow')