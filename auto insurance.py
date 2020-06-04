# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:34:10 2019

@author: Shrutika
"""


import pandas as pd
import seaborn as sns
import numpy as np
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\auto_insurance_sweden.csv')
dc=df.columns
df.columns
cor=df.corr().values
sns.heatmap(df.corr(),annot=True)
r,c=np.triu_indices(cor.shape[0],k=1)
idx=cor[r,c].argsort()
a=np.c_[dc[r[idx]],dc[c[idx]],cor[r,c][idx]]
df1=pd.DataFrame(a,columns=['Independent','Dependent','Values']) 
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
df2=df1.loc[df1['Values']>0.4]
for i in range(len(df2)):
    x=pd.DataFrame(df[df2.Independent[i]])
    y=pd.DataFrame(df[df2.Dependent[i]])
    obj.fit(x,y)
    pr=obj.predict(x)
    from sklearn.metrics import r2_score
    acc=r2_score(y,pr)
    print(df2.Independent[i],'and',df2.Dependent[i],'has accuracy',acc)
