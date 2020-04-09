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


#Second part

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList,
 columns=['Names','Grades','BS Degrees','Ms Degrees','PhD Degrees'])
df

countdf = df.count() # number of values
meandf = df.mean() # arithmetic average
stddf = df.std() # standard deviation
mindf = df.min() # minimum
maxdf = df.max() # maximum
q25df = df.quantile(.25) # first quartile
q50df = df.quantile(.5) # second quartile
q75df = df.quantile(.75) # third quartile

SummaryStat = zip(countdf,meandf,stddf,mindf,maxdf,q25df,q50df,q75df)
df = pd.DataFrame(data=SummaryStat,
 columns=['Count','Mean','Std Dev','Min','Max', 'q25','q50','q75'],
 index = ['Grades', 'BS Degrees', 'MS Degrees', 'PhD Degrees' ])
print(df)