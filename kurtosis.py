# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:57:14 2019

@author: Shrutika
"""
import numpy as np
import scipy.stats as s
d=np.random.randint(1,10,100)
print(s.kurtosis(d))
e=np.mean(d)