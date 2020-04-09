# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:15:58 2020

@author: alyss
"""

#First Part
import pandas as pd
import matplotlib.pyplot as plt
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
 

