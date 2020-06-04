# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:38:06 2019

@author: Shrutika
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
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
from sklearn.svm import LinearSVC
obj=LinearSVC()
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,pr)
from sklearn.naivebayes import GaussianMB
obj=GaussianMB()
obj.fit(x,y)
pr1=obj.predict(x)