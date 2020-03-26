# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:52:06 2020

@author: alyss
"""

## VISUALIATIONS USING SEABORN
#Visualization Two
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
# Create empty figure
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
# set the x and y axis range
plt.xlim(0, 11)
plt.ylim(-2, 2)
plt.axis('tight')
#add title
plt.title('Plotting data using sin and cos')


#Visualization three
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('classic')
plt.style.use('seaborn-whitegrid')
# Create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],
size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
# Plot the data with seaborn
sns.distplot(data['x'])
sns.distplot(data['y']);

#Visualization Four - Kernel Density Plot
for col in 'xy':
    sns.kdeplot(data[col], shade=True)
    
#Visualization Five - Two-dimensional Kernel Density Plot
sns.kdeplot(data);

#Visualization Six - Joint-distribution Plot  
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde');
    
#Visualization Seven - Hexagonally based histogram
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')

#Visualization Eight - Multidimensional Relationships Graphs
sns.pairplot(data);
