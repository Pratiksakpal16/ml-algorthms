# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:55:39 2019

@author: Shrutika
"""
import numpy as np
import scipy.stats as t
d=np.random.randint(1,10,100)
print(t.skew(d))
