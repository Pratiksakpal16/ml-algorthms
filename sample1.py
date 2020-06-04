# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:45:32 2019

@author: Shrutika
"""

import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\sample1.xlsx')
df.columns
df.head()
x=pd.DataFrame(df.Body_weight)
y=pd.DataFrame(df.Brain_weight)
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
obj.fit(x,y)
pr=obj.predict(x)
e=int(input("enter value"))
f=obj.predict([[e]]) 
print("if bodyweight is {} then brain weight is{}".format(e,abs(f)))
