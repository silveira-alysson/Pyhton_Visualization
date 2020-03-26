# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:57:35 2020

@author: alyss
"""

##Plot in Python - basic plots
import pandas as pd 
import numpy as np
df = pd.DataFrame(np.random.randn(200,6),
                  index= pd.date_range('1/9/2009', periods=200), 
                  columns= list('ABCDEF'))
df.plot(figsize=(20, 10)).legend(bbox_to_anchor=(1, 1))

#Direct ploting
import pandas as pd 
import numpy as np
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May'])
df.plot.bar(figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))

#stacked bar plot
import pandas as pd
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May']) 
df.plot.bar(stacked=True, figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))

#Horizontal bar plot
import pandas as pd
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May']) 
df.plot.barh(stacked=True,figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))

#using bar bins attributes
import pandas as pd
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May'])
df.plot.hist(bins=20, figsize=(10,8)).legend(bbox_to_anchor=(1.2, 1))

#Multiple Histograms per Column
import pandas as pd
import numpy as np
df=pd.DataFrame({'April':np.random.randn(1000)+1,'May':np.random.randn(1000),
                 'June': np.random.randn(1000) - 1}, columns=['April','May', 'June'])
df.hist(bins=20)

#Boxplot
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5),
columns=['Jan','Feb','March','April', 'May'])
df.plot.box()


# Area Plot
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5),
columns= ['Jan','Feb','March','April', 'May'])
df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3, 1))

#Scatter plot
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5),columns= ['Jan','Feb','March','April', 'May'])
df.plot.scatter(x='Feb', y='Jan', title='Temperature over two months ')


#Exercises plots
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
df = pd.DataFrame()
df ['Name'] =salesMen
df ['Mobile_Sales'] = Mobile_Sales
df['TV_Sales']=TV_Sales
df.set_index("Name",drop=True,inplace=True)
df.plot.bar( figsize=(20, 10), rot=0).legend(bbox_to_anchor=(1.1, 1)) 
plt.xlabel('Salesmen') 
plt.ylabel('Sales')
plt.title('Sales Volume for two salesmen in \nJanuary and April 2017')
plt.show()

df.plot.pie(subplots=True)

df.plot.box()

df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3, 1))

df.plot.bar(stacked=True, figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


#pushing Python_Visualization.py file to my GitHub
!git init
!git add "Python_Visualization.py"
!git commit -m "My commit"
!git remote add origin https://github.com/silveira-alysson/Pyhton_Visualization.git
!git push -u origin master