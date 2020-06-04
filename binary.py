# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:18:49 2019

@author: Shrutika
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Regression_analysis\binary.csv')
dc=df.columns
from sklearn.linear_model import LogisticRegression
obj=LogisticRegression()
x=pd.DataFrame(df.gre)
x['gpa']=df.gpa
x['rank']=df['rank']
y=pd.DataFrame(df.admit)
obj.fit(x,y)
pr=obj.predict(x)
from sklearn.metrics import confusion_matrix
c=confusion_matrix(pr,y)
acc=((c[0,0]+c[1,1]/len(df))*100)
sns.heatmap(c,annot=True)
from sklearn import metrics
yprob=obj.predict_proba(x)[::,1]
fpr,tpr,t=metrics.roc_curve(y,yprob)
auc=metrics.roc_auc_score(y,yprob)
plt.plot(fpr,tpr)
