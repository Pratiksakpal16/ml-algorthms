# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:40:52 2019

@author: Shrutika
"""

import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\sample2.xlsx')
df.columns
df.head()
x=pd.DataFrame(df.Age)
x['weight']=df.Weight
y=pd.DataFrame(df['Blood Fat Content'])
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
obj.fit(x,y)
pr=obj.predict(x)
pr=obj.predict(x)
e=int(input("enter age"))
h=int(input("enter weight"))
f=obj.predict([[e,h]])
print("if age is {} and weight is {} then blood fat content is {}".format(e,h,abs(f)))
