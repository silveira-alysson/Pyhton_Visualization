# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:30:50 2020

@author: alyss
"""

#First Part
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.hist(column="age", by="gender")

