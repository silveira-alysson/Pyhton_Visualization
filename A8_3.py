# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:49:42 2020

@author: alyss
"""


#Third Part
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
plt.scatter(df['hours'], df['grade'])

#The number of study hours and the grades seems to be positively correlated.