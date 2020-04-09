# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:15:58 2020

@author: alyss
"""

#First Part
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
 columns=['Names', 'Grades'])
df.plot()


df.plot()
displayText = "Wow!"
xloc = 0
yloc = df['Grades'].min()
xtext = 250
ytext = 0
plt.annotate(displayText,
 xy=(xloc, yloc),
 arrowprops=dict(facecolor='black',
 shrink=0.05), 
 xytext=(xtext,ytext),
 xycoords=('axes fraction', 'data'),
 textcoords='offset points')
 
 
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

