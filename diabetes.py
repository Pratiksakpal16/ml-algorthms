# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:14:23 2019

@author: Shrutika
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\diabetes.csv')
df.columns
obj=LogisticRegression()
x=pd.DataFrame(df.Glucose)
x['bp']=(df.BloodPressure)
x['ins']=(df.Insulin)
x['dpf']=(df.DiabetesPedigreeFunction)
x['age']=(df.Age)
y=pd.DataFrame(df.Outcome)
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import confusion_matrix
c=confusion_matrix(pr,y)
acc=((c[0,0]+c[1,1])/len(df))*100
print('accuracy:',acc)
glucose=float(input("enter glucose value"))
bloodpressure=float(input("enter bloodpressure value"))
insulin=float(input("enter insulin value"))
diabetespedigreefunction=float(input("enter diabetespedigreefunctionvalue"))
age=int(input("enter age"))
p=obj.predict([[glucose,bloodpressure,insulin,diabetespedigreefunction,age]])
if p==0:
    print("Need not visit Doctor")
else:
    print("Need to visit Doctor")

