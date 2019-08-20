#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:13:48 2019

@author: Renato Naville Watanabe
"""

import numpy as np
import matplotlib.pyplot as plt

diaTot = 1000
dias = np.arange(0, diaTot, 1)
coelho = np.zeros(len(dias))
lobo = np.zeros(len(dias))

coelho[0] = 1
lobo[0] = 2
repCoelho = 0.7
taxaPred = 0.7
morteLobo = 0.8
repLobo = taxaPred


for i in range(1, len(coelho)):
    dcoelho = repCoelho*coelho[i-1] - taxaPred*lobo[i-1]*coelho[i-1]
    dlobo = repLobo*lobo[i-1]*coelho[i-1] - morteLobo*lobo[i-1]
    
    coelho[i] = coelho[i-1] + dcoelho
    lobo[i] = lobo[i-1] + dlobo
    
    if coelho[i]<0: coelho[i]=0
    if lobo[i] < 0: lobo[i]=0
    
plt.figure()
plt.plot(dias, coelho, 'g-.')
plt.plot(dias, lobo, 'r--')
plt.show()