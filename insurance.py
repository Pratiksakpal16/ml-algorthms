# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:45:13 2019

@author: Shrutika
"""
import matplotlib.pyplot as plt
import pandas as pd
dt=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\EDA-Datasets\Insurance.csv')
d.columns
d.shape
d.head()
d.tail()
d['Y']=d['Y'].str.replace('','')