# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:07:57 2019

@author: Shrutika
"""
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\pratikproject\insurance.csv')
dc=df.columns
cor=df.corr().values
sns.heatmap(df.corr(),annot=True)
r,c=np.triu_indices(cor.shape[0],k=1)
idx=cor[r,c].argsort()
a=np.c_[dc[r[idx]],dc[c[idx]],cor[r,c][idx]]
df1=pd.DataFrame(a,columns=['Independent','Dependent','Values']) 
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
le=LabelEncoder()
sex=le.fit_transform(df.sex)
smoking=le.fit_transform(df.smoker)
region=le.fit_transform(df.region)
x=pd.DataFrame(df.age)
x['sex']=sex
x['bmi']=df.bmi
x['children']=df.children
x['smoking']=smoking
x['region']=region
y=pd.DataFrame(df.charges)
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import r2_score
acc=r2_score(y,pr)*100
age=int(input("enter value"))
sex=str(input("enter value"))
if sex=="Male":
    sex=1
else:
    sex=0
bmi=float(input("enter value"))
children=int(input("enter value"))
smoking=str(input("enter value"))
if smoking=="Yes":
    smoking=1
else:
    smoking=0
region=str(input("enter region"))
if region=="souteast":
    region=1
elif region=="southwest":
    region=2
elif region=="northeast":
    region=3
else:
    region=4  
l=pd.DataFrame([age])
l["sex"]=sex
l["bmi"]=bmi
l["children"]=children
l["smoking"]=smoking
l["region"]=region
p=obj.predict(l)
p=abs(p)
