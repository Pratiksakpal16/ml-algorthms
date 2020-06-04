# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:34:59 2019

@author: Shrutika
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dt=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\EDA-Datasets\drinks.csv')
dt.columns
beer=np.sum(dt['beer_servings'])
spirit=np.sum(dt['spirit_servings'])
wine=np.sum(dt[ 'wine_servings'])
li=[beer,spirit,wine]
print('list',li)
x=('beer','spirit','wine')
plt.figure(figsize=(10,10))
plt.pie(li,labels=x,autopct='%2.2f%%',radius=1.0)
plt.title('Drinks')
