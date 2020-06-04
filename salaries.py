# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:41:57 2019

@author: Shrutika
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\New folder\salaries.csv')
df.columns
le=LabelEncoder()
c=le.fit_transform(df.company)
e=le.fit_transform(df.job)
f=le.fit_transform(df.degree)
x=pd.DataFrame(c)
x['job']=e
x['degree']=f
y=pd.DataFrame(df.salary_more_then_100k)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(x,y)
pr=model.predict(x)
from sklearn.metrics import accuracy_score
accuracy_score(y,pr)
