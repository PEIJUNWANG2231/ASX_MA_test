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
    path='D:/Python Codes Lib/ASX database/'
    code=str(code)
    df = pd.read_csv(path+code+'.csv')
    return df

def Data_Visualize(df,start_date,end_date):

    list1=df['Date'].tolist()
    
    start=list1.index(start_date)
    
    end=list1.index(end_date)
    #jaw line
    trace1 ={
            'x':df['Date'][start:end].tolist(),
            'y':df['jaw'][start:end].tolist(),
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
            'x':df['Date'][start:end].tolist(),
            'y':df['teeth'][start:end].tolist(),
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
            'x':df['Date'][start:end].tolist(),
            'y':df['lips'][start:end].tolist(),
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
            'x':df['Date'][start:end].tolist(),
            "close":df['Close'][start:end].tolist(),
            "decreasing": {"line": {"color": "red"}},
            "high":df['High'][start:end].tolist(),
            "increasing": {"line": {"color": "green"}},
            "low":df['Low'][start:end].tolist(),
            "name": "AMU",
            "open":df['Open'][start:end].tolist(),
            "type": "candlestick", 
            "yaxis": "y2"
            }


    data = [trace1,trace2,trace3,trace4]

    # It should be opened in website
    py.iplot(data, filename='simple_candlestick')

def main(code,start_date,end_date):
    df=init(code)
    Data_Visualize(df,start_date,end_date)

if __name__ == '__main__':
    main('CBA','2000-01-01','2001-01-01')