# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:45:48 2020

@author: alyss
"""

# Second part

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)

#: 1. Tests for the relationship between just grade and age; 

result = sm.ols(
 formula='grade ~ age - 1',
 data=df).fit()
print(result.summary())

#2. Tests for the relationship between just grade and exercise; and 

result = sm.ols(
 formula='grade ~ exercise - 1',
 data=df).fit()
print(result.summary())

#3. Tests for the relationship between just grade and study.

result = sm.ols(
 formula='grade ~ hours - 1',
 data=df).fit()
print(result.summary())

#If you had to pick just one, which one do you like best?

#I would pick the model with only age as an independent variable, as its R-Squared is 0.976 and the variable is statistically significant.