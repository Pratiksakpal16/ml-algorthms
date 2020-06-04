# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:20:59 2019

@author: Shrutika
"""
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder 
le=LabelEncoder()
le1=LabelEncoder()
le2=LabelEncoder()
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\New folder\play.csv')
df.columns
obj=DecisionTreeClassifier()
weather=le.fit_transform(df.Weather)
temp=le1.fit_transform(df.Temp)
play=le2.fit_transform(df.Play)
df['nt']=temp
df['np']=play
b={}
a=df['Weather'].unique()
for i in range(len(df)):
    for j in range(len(a)):
        if df.Weather[i]==a[j]:
            b[a[j]]=df.nw[i]
c={}
c1=df['Temp'].unique()
for i in range(len(df)):
    for j in range(len(c1)):
        if df.Temp[i]==c1[j]:
            c[c1[j]]=df.nt[i]
d={}
d1=df['Play'].unique()
for i in range(len(df)):
    for j in range(len(d1)):
        if df.Play[i]==d1[j]:
            d[d1[j]]=df.np[i]            
x=pd.DataFrame(weather)
x['Temp']=temp
y=pd.DataFrame(play)
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import r2_score
r2_score(y,pr)
acc=r2_score(y,pr)*100
w=input("enter weather type:")
t=input("enter temperature type:")
for i in b:
    if w==i:
        w=b[i]
for i in c:
    if t==i:
        t=c[i]
p=obj.predict([[w,t]])        
for i in d:
    if p==d[i]:
        print(i)
if p==0:
    print("i can go out to play")
else:
    print("i cannot go out to play")