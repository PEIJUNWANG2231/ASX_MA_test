# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:54:59 2019

@author: XPS15
"""
import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASXPartTwoAveragerGluing import AveragerGluing
from ASXPartSevenResult import IterAveragerGluing
from ASXPartFourMatchUpFractals import MatchUpFractals
from ASXPartFiveMatchDownFractals import MatchDownFractals
from ASXPartSixEnterAndLossPoint import EnterPoint,StopLossPoint
import pandas as pd
import datetime
import winsound

#遍历所有的股票，输出到一张excel中
def DataFrame(code):
    
    df=pd.read_csv('D:/Python Codes Lib/ASX database/'+code+'.csv')
    
    list1=AveragerGluing(df)
    
    li3=[]
    
    li1=MatchUpFractals(df,list1)
    
    for i in range(len(li1)):
        if li1[i]==0:
            li3.append(i)
    
    li2=MatchDownFractals(df,list1)
    
    for i in range(len(li2)):
        if li2[i]==0:
            li3.append(i)
    
    #同时再 list1，li1 和li2 里面剔除掉对应的情况
    for i in li3:
        del list1[i]
        
    m=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Var1',
 'jaw', 'teeth', 'lips', '5&8', '8&13', 'compare', 'daily_pct']
    
    df1=pd.DataFrame(columns = m)
    
    list2=IterAveragerGluing(df)
    
    li1=MatchUpFractals(df,list1)
    
    li2=MatchDownFractals(df,list1)
    
    dict1=EnterPoint(df)
    
    dict2=StopLossPoint(df)
    
    for i in range(len(list1)):
        df2=df.iloc[list1[i]:list1[i]+1,:]
        df2['result']=list2[i]
        df2['code']=code
        df2['StopLoss']=dict2[li2[i]]
        df2['Enter']=dict1[li1[i]]
        df2['StopLossPct']=(dict1[li1[i]]-dict2[li2[i]])/dict1[li1[i]]
        frames=[df1,df2]
        df1=pd.concat(frames)

    return df1

def set():
    df1=pd.read_csv('D:/Python Codes Lib/ASX list of code/20190201-asx300.csv')

    list1=list(df1.loc[:,'Code'])
    
    list2=[]
    
    for i in list1:
        try:
            df=DataFrame(i)
            list2.append(df)
        except:
            FileNotFoundError
    df1=pd.concat(list2)
    df1.to_csv('D:/Python Codes Lib/ASX.csv')
    return df1

def main():
    start = datetime.datetime.now()
    set()
    df1=pd.read_csv('D:/Python Codes Lib/ASX.csv')
    
    df1=df1[~df1['result'].str.contains('no enter')]
    df3=df1[~df1['result'].str.contains('no result')]
    
     
    df2=df1[~df1['result'].str.contains('stop loss')]
    
    #sussecc rate
    SR=len(df2)/len(df1)
    
    print('sussecc rate is %2f' %SR)
    
    #the amount of no result
    NE=(len(df1)-len(df3))/len(df1)
    
    if NE >0.05:
        print('the amount of no result is too many, is %2f' %NE)
    else:
        print('no result is %2f' %NE)
    
    df3.to_csv('D:/Python Codes Lib/ASX.csv')
    end = datetime.datetime.now()
    print(end-start)
    
    #warning
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    return SR

if __name__ == '__main__':
    main()








