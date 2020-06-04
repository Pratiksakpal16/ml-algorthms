# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:48:56 2019

@author: Shrutika
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\EDA-Datasets\P4-Movie-Ratings.csv')
genre=input("Enter name of genre:")
year=int(input("Enter Year:"))
budget=0
for i in range(len(df)):
    if df['Genre'][i]==genre and df['Year of release'][i]==year:
        budget=budget+df['Budget (million $)'][i]
print(budget)
