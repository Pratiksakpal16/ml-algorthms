# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:36:31 2019

@author: Shrutika
"""
import matplotlib.pyplot as plt
x=(10,20,30)
y=(1,2,3)
plt.scatter(x,y,marker='*',s=50)
plt.bar(x,y)
plt.xlabel('temp')
plt.ylabel('values')
plt.title('weather')