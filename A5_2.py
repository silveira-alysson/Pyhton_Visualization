# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:45:01 2020

@author: alyss
"""

#Second part

import pandas as pd
import numpy as np
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