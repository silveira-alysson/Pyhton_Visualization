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

#Third Part
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
plt.scatter(df['hours'], df['grade'])

#The number of study hours and the grades seems to be positively correlated.