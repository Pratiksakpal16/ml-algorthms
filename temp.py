# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello world")
import numpy as np
a=np.arange(100)
b=np.random.randint(1,10,50)
print(b)
b=b.reshape(-1,1)
a=np.random.randn(3,3)
b=np.random.rand(3,2)
import pandas as pd
L=[1,2,3,4]
df=pd.DataFrame(L,columns=['ID'],index=['a','b','c','d'])
df=df.reindex(['a','b','c','d','e','f'])
df.isna()
df.isnull()
df=df.fillna(method='pad')
df=df.fillna(method='backfill')
L={1:'abc',2:'def',3:'ghi'}
d=pd.DataFrame(L,index=['a','b','c','d'])
d=['mobileno']=[123,456,789,101]