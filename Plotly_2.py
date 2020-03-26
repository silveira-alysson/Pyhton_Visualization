# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:56:15 2020

@author: alyss
"""

## dynamic Plotly graph drawn in a web browser
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
print (__version__)


import plotly.graph_objs as go
plot([go.Scatter(x=[95, 77, 84], y=[75, 67, 56])])
'file:///home/nbuser/library/temp-plot.html'