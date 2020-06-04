# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:44:02 2019

@author: Shrutika
"""
import matplotlib.pyplot as plt
x=['A','B','C','D','E','F','G','H','I']
y=[113,85,90,150,149,88,93,115,135]
plt.figure(figsize=(15,5))
plt.hist(y)
plt.xlabel('temp')
plt.ylabel('values')
plt.title('patent')
plt.figure(figsize=(15,5))
plt.hist(y,bins=[50,100,125])