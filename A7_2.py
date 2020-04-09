# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:48:57 2020

@author: alyss
"""

 
 #Second Part
 
from IPython import get_ipython
import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior',
 'Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades,status)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades', 'Status'])

get_ipython().run_line_magic('matplotlib', 'inline')
df = df.set_index(df['Status'])
df.plot(kind="bar")
