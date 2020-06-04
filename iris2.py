# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:47:51 2019

@author: Shrutika
"""

import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\iris.csv')
df.columns
a=df.corr()
import seaborn as sns
cor=df.corr().values
sns.heatmap(df.corr(),annot=True)
x=pd.DataFrame(df['Petal.Length'])
y=pd.DataFrame(df['Petal.Width'])
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import r2_score
acc=r2_score(y,pr)
print("acc",acc)
