# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:26:10 2019

@author: Shrutika
"""

import matplotlib.pyplot as plt
x=('TR','HR','MB')
y=(1400,1500,500)
plt.pie(y,labels=x,autopct='%2.2f%%',radius=1.2)
plt.xlabel('temp')
plt.ylabel('values')
plt.title('weather')