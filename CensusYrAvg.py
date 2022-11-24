# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Joshua Harrington
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\josh1\OneDrive\Documents\Python\PythonLearning\PythonLearning\CO_Census.csv",engine='python',encoding='latin1')

df.drop(index = 0, inplace = True)
columns = df.columns



columns_original = df.columns
df.drop(['POPESTIMATE042020','ESTIMATESBASE2010','POPESTIMATE2010'], axis = 1, inplace = True)
columns = df.columns
first = columns.get_loc('CENSUS2010POP')
last = columns.get_loc('POPESTIMATE2020')
name = columns.get_loc('NAME')

df = np.array(df)
change = np.zeros((len(df),(last-first)-1))

for i in range(len(df)):
    k = 0
    for j in range(first, last-1):
        try:
            change[i,k] = ((df[i,j+1]-(df[i,j]))/df[i,j])*100
        except:
            change[i,k] = 0
        k = k+1
    
        
average_change = np.zeros((change.shape[0],1))
        
for l in range(len(change)):
    average_change[l] = np.mean(change[l,:])
    
df = pd.DataFrame(df)

df["Average Change"] = average_change


df.drop_duplicates(subset = name, keep = "first", inplace = True)

population_sorted = df.sort_values(by = [last], ascending = False)




    
    
    
     
     
