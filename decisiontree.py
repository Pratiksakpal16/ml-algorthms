# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:14:41 2019

@author: Shrutika
"""
import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\iris.csv')
df.columns
x=pd.DataFrame(df['Sepal.Length'])
x['sw']=df['Sepal.Width']
x['pl']=df['Petal.Length']
x['pw']=df['Petal.Width']
y=pd.DataFrame(df['Species'])
from sklearn.tree import DecisionTreeClassifier
obj=DecisionTreeClassifier()
obj.fit(x,y)
obj.predict(x)

