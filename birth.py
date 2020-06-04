import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\EDA-Datasets\US_births_1994-2003_CDC_NCHS.csv')
uy=dt['year'].unique()
type(uy)
de=list(uy)
b=0
l=[]
for i in range(len(de)):
    d=dt.loc[dt['year']==de[i]]
    b=np.sum(d.births)
    l.append(b)
print(l)
plt.figure(figsize=(10,10))
plt.pie(l,labels=de,autopct='%2.2f%%',radius=1.0)
plt.title('Births')
year=int(input('enter year'))
d=dt.loc[dt['year']==year]
a=d.sample(20)   
import scipy.stats as s
z=s.norm.ppf(q=0.975)
moe=z*np.std(a)/np.sqrt(len(a))
UL=moe+np.mean(a)
LL=moe-np.mean(a)         
print(UL)
print(LL)
    