# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:55:59 2019

@author: Shrutika
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Clustering\shopping_data (1).csv')
df.columns
x=pd.DataFrame(df['Age'])
y=pd.DataFrame(df['Annual Income (k$)'])
from sklearn.preprocessing import StandardScaler,normalize
scaler=StandardScaler()
xscale=scaler.fit_transform(x)
x_normalized=normalize(xscale)
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
princi=pca.fit_transform(x_normalized)
princi_df=pd.DataFrame(princi)
from sklearn.Cluster import DBSCAN
obj=DBSCAN(eps=0.0375,min_samples=3).fit(princi_df)
obj.labels_
plt.scatter(df['Age'],df['Annual Income (k$)'],c=obj.labels_,cmap='rainbow')