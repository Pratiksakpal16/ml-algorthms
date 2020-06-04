# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:50:09 2019

@author: Shrutika
"""

from scipy.stats import chi2_contingency
t=[[10,20,30],[6,9,17]]
stats,p,dof,expected=chi2_contingency(t)
alpha=1-0.95
if alpha<=p:
    print("select alternate hypothesis and reject null hypothesis")
else:
    print("null hypothesis")