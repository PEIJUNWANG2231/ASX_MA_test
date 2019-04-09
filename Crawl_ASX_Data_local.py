# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:10:05 2019

@author: XPS15
"""
# step 1
# Data preparation of further data manipulating 
# save the CSV in local laptop 

import pandas as pd
import pandas_datareader.data as web
import datetime
import fix_yahoo_finance as yf
import numpy as np

#SMA is a type of MA, it could be call by talib
def SMA(close,n,m=1):
    result = np.array([np.nan]*len(close))
    result[n-2]=close[:n-1].mean()
    for i in range(n-1,len(close)):
        result[i]=(m*close[i]+(n-m)*result[i-1])/n
    return result

#basic operation of financial market data from Yahoo APIs  
def Alligator(df,n=1):
    
    df['Var1']=(df['High']+df['Low'])/2
    
    average=[5,8,13] #fibonacci squence:5,8,13 
    moves=[3,5,8]
    names=['jaw','teeth','lips']
    
    #produce the three SMA: 5,8,13, and shift forward 3,5,8 unit
    for i in range(3):
        df[names[i]]=SMA(df['Var1'],average[i])
        df[names[i]]=df[names[i]].shift(periods=moves[i])
    
    df['5&8']=df['jaw']-df['teeth']
    df['8&13']=df['teeth']-df['lips']
    df['5&8']=abs(df['5&8'])
    df['8&13']=abs(df['8&13'])
    
    #均线粘合的差值由close来决定
    
    #compare data is decided by the close price
    
    df['compare']=((df['Close']/10).astype(int)+n)*0.01
    df['daily_pct']=abs(df['Open']-df['Close'])/df['Close']
    df=df.dropna()
    return df


#use API to get the related data by code
def csv(code):
    yf.pdr_override() 
    end=datetime.date.today()
    start='2000-01-01'
    end=end.strftime("%Y-%m-%d")
        
    read_code=code+'.AX'
    df=web.get_data_yahoo(read_code,start,end)
    df=Alligator(df)
    m='D:\\Python Codes Lib\\ASX database'
    n=code
    
    df.to_csv(m+'\\'+n+'.csv')

#change the name of csv to gain the different list of ASX set
df1=pd.read_csv('D:/Python Codes Lib/ASX list of code/20190201-asx300.csv')

list1=list(df1.loc[:,'Code'])

def main():
    list2=[]
    for i in list1:
        try:
            csv(i)
        except:
            ValueError
            list2.append(i)
    return list2
        
if __name__ == '__main__':
    main()


