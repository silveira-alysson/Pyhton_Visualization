# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:24:03 2020

@author: alyss
"""
import pandas as pd
import numpy as np
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.tail()

df['genderBin'] = np.where(df['gender']=='female',1, 0)
df.tail(10)

import statsmodels.formula.api as sm

result = sm.ols(
 formula='grade ~ exercise + hours',
 data=df).fit()
print(result.summary())

result = sm.ols(
 formula='grade ~ exercise + hours + genderBin',
 data=df).fit()
print(result.summary())


#The R-Squared has increased from 0.664 to 0.665, but the new variable is not statistically significant at a 95% confidence interval.

