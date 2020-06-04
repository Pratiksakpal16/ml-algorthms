# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:57:24 2019

@author: Shrutika
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\New folder\loan_data_set.csv')
df.columns
df=df.dropna()
le=LabelEncoder()
gender=le.fit_transform(df.Gender)
married=le.fit_transform(df.Married)
education=le.fit_transform(df.Education)
selfemployed=le.fit_transform(df.Self_Employed)
age=le.fit_transform(df.Property_Area)
x=pd.DataFrame(gender)
x['married']=married
x['education']=education
x['selfemployed']=selfemployed
x['age']=age
y=pd.DataFrame(df.Loan_Status)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25)
obj=DecisionTreeClassifier()
obj.fit(xtrain,ytrain)
pr=obj.predict(xtest)
from sklearn.metrics import accuracy_score
acc=accuracy_score(ytest,pr)
acc=print('accuracy:',acc)
gender=input("enter gender")
married=input("enter martial status")
education=input("enter education")
selfemployed=input("enter selfemployed or not")
age=int(input("enter age"))
p=obj.predict([[gender,married,education,selfemployed,age]])
if p==0:
    print("person can get loan")
else:
    print("person cannot get loan")