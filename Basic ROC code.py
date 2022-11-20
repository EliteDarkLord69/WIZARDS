# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('LA_Census.csv')
A = [0]*743


poop = df.sort_values(by ="POPESTIMATE042020", ascending = True)
x = 0
for x in range(743):
    a = df.iloc[x,23]
    b = df.iloc[x,10]

    rof = (a-b)/b
    A[x] = rof*100
   
    
    

df["roc"] = A




    
