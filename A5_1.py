# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:01:37 2020

@author: alyss
"""

#First part

import pandas as pd
import numpy as np
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.tail()
sample = df.take(np.random.permutation(len(df))[:500])


