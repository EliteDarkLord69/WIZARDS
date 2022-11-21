# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:46:07 2022

@author: JChaparro
"""

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('LA_Census.csv')
del df["POPESTIMATE042020"]
df = df.drop(df.columns[[0, 1,2, 3,4,5,6,7,10,11]], axis=1)

A = [0]*len(df)
AA = [0]*10
s = df.columns.get_loc("POPESTIMATE2020")
t = df.columns.get_loc("POPESTIMATE2010")


for p in range(len(df)):
    t = df.columns.get_loc("POPESTIMATE2010")
    i=0
    for x in range(10):
        a = df.iloc[p,t+1]
        b = df.iloc[p,t]

        rof = (a-b)/b
        AA[i] = rof*100
        i = i+1
        t = t+1
    
    A[p] = np.mean(AA)

   
    
    

df["roc"] = A
df = df.drop_duplicates()
