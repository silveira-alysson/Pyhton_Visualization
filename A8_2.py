# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:49:37 2020

@author: alyss
"""
#Second Part
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']

plt.pie(df['TotalDemerits'],
 labels=df['Names'],
 explode=(0,0,0,0.15,0),
 startangle=90,
 autopct='%1.1f%%',)
plt.axis('equal')
plt.show()

