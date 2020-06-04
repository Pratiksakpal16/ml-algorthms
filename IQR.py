# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:52:09 2019

@author: Shrutika
"""
import numpy as np
d=np.random.randint(1,10,100)
q1=np.percentile(d,25)
q3=np.percentile(d,75)
print(q3-q1)
