# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:18:11 2019

@author: Shrutika
"""

import pandas as pd
import seaborn as sns
import numpy as np
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\Advertising.csv')
dc=df.columns
cor=df.corr().values
sns.heatmap(df.corr(),annot=True)
r,c=np.triu_indices(cor.shape[0],k=1)
idx=cor[r,c].argsort()
a=np.c_[dc[r[idx]],dc[c[idx]],cor[r,c][idx]]
df1=pd.DataFrame(a,columns=['Independent','Dependent','Values']) 
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
x=pd.DataFrame(df.TV)
y=pd.DataFrame(df.Sales)
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import r2_score
acc=r2_score(y,pr)*100
TV=float(input("enter value"))
obj.predict([[TV]])
x['News']=df.Newspaper
Newspaper=float(input("enter value"))
p=obj.predict([[TV,Newspaper]])