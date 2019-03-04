# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:56:00 2019

@author: XPS15
"""

import plotly.plotly as py
import pandas as pd

import plotly 

def init(code):
    global df
    plotly.tools.set_credentials_file(username='PEIJUNWANG2231', api_key='gTOZ74BxV9KnKWsJfL2t')
    path='D:/ASX Trading System/ASX Temporary Data/'
    code=str(code)
    df = pd.read_csv(path+code+'.csv')
    return df


#jaw line
trace1 ={
        'x':df['Date'].tolist(),
        'y':df['jaw'].tolist(),
        "legendgroup": "alligator",
        "line": {
                "color": "green", 
                "width": 1
                },
        "mode": "lines", 
        "name": "jaw", 
        "showlegend": True, 
        "text": "", 
        "type": "scatter", 
        "yaxis": "y2"
        }
    
#teeth line    
trace2 ={
        'x':df['Date'].tolist(),
        'y':df['teeth'].tolist(),
        "legendgroup": "alligator",
        "line": {
                "color": "red", 
                "width": 1
                },
        "mode": "lines", 
        "name": "teeth", 
        "showlegend": True, 
        "text": "", 
        "type": "scatter", 
        "yaxis": "y2"
        }

#lips line
trace3 ={
        'x':df['Date'].tolist(),
        'y':df['lips'].tolist(),
        "legendgroup": "alligator",
        "line": {
                "color": "blue", 
                "width": 1
                },
        "mode": "lines", 
        "name": "lips", 
        "showlegend": True, 
        "text": "", 
        "type": "scatter", 
        "yaxis": "y2"
        }
  
#candlestick      
trace4 ={
        'x':df['Date'].tolist(),
        "close":df['Close'].tolist(),
        "decreasing": {"line": {"color": "red"}},
        "high":df['High'].tolist(),
        "increasing": {"line": {"color": "green"}},
        "low":df['Low'].tolist(),
        "name": "AMU",
        "open":df['Open'].tolist(),
        "type": "candlestick", 
        "yaxis": "y2"
        }


data = [trace1,trace2,trace3,trace4]

# It should be opened in website
py.iplot(data, filename='simple_candlestick')
