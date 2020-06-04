# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:32:11 2019

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
multi.fit(x,y)
pr=multi.predict()
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import r2_score
acc=r2_score(y,pr)*100
SepalLength=float(input("enter value"))
SepalWidth=float(input("enter value"))
PetalLength=float(input("enter value"))
PetalWidth=float(input("enter value"))
p=obj.predict([[SepalLength,SepalWidth,PetalLength,PetalWidth,]])
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
obj.fit(x,y)
pr=obj.predict(x)