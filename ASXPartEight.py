# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:54:59 2019

@author: XPS15
"""
#ASXPartEight

import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASXPartTwoAveragerGluing import AveragerGluing_5_8,AveragerGluing_8_13,AveragerGluing_5_8_13
from ASXPartSevenResult import IterAveragerGluing
from ASXPartFourMatchUpFractals import MatchUpFractals
from ASXPartFiveMatchDownFractals import MatchDownFractals
from ASXPartSixEnterAndLossPoint import EnterPoint,StopLossPoint
import pandas as pd
import datetime
import winsound

#遍历所有的股票，输出到一张excel中
# para: code and list1
# code: stock code
# code ralated list1 = AveragerGluing_5_8
#                    = AveragerGluing_8_13
#                    = AveragerGluing_5_8_13
def DataFrame(code,list1):
    
    df=pd.read_csv('D:/Python Codes Lib/ASX database/'+code+'.csv')
    
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
        del li1[i]
        del li2[i]
        
    m=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Var1',
 'jaw', 'teeth', 'lips', '5&8', '8&13', 'compare', 'daily_pct']
    
    df1=pd.DataFrame(columns = m)
    
    list2=IterAveragerGluing(df,list1)
    
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

def operate_5_8():
    start = datetime.datetime.now()
    df1=pd.read_csv('D:/Python Codes Lib/ASX list of code/20190201-asx300.csv')

    list1=list(df1.loc[:,'Code'])
    
    #create 5&8 df
    list2=[]
    
    for i in list1:
        try:
            dataframe1=pd.read_csv('D:/Python Codes Lib/ASX database/'+i+'.csv')
            li1=AveragerGluing_5_8(dataframe1)
            df=DataFrame(i,li1)
            list2.append(df)
        except:
            FileNotFoundError
    df1=pd.concat(list2)
    df1['type']='5&8'
    end = datetime.datetime.now()
    print(end-start)
    return df1
    
def operate_8_13():    
    start = datetime.datetime.now()
    df1=pd.read_csv('D:/Python Codes Lib/ASX list of code/20190201-asx300.csv')

    list1=list(df1.loc[:,'Code'])
    #create 8&13 df
    list3=[]
    
    for i in list1:
        try:
            dataframe2=pd.read_csv('D:/Python Codes Lib/ASX database/'+i+'.csv')
            li2=AveragerGluing_8_13(dataframe2)
            df=DataFrame(i,li2)
            list3.append(df)
        except:
            FileNotFoundError
    df2=pd.concat(list3)
    df2['type']='8&13'
    end = datetime.datetime.now()
    print(end-start)
    return df2

def operate_5_8_13():    
    start = datetime.datetime.now()
    df1=pd.read_csv('D:/Python Codes Lib/ASX list of code/20190201-asx300.csv')

    list1=list(df1.loc[:,'Code'])
    #create 5&8&13 df
    list4=[]
    
    for i in list1:
        try:
            dataframe3=pd.read_csv('D:/Python Codes Lib/ASX database/'+i+'.csv')
            li3=AveragerGluing_5_8_13(dataframe3)
            df=DataFrame(i,li3)
            list4.append(df)
        except:
            FileNotFoundError
    df3=pd.concat(list4)
    df3['type']='5&8&13'
    end = datetime.datetime.now()
    print(end-start)
    return df3


def main():
    df1=operate_5_8()
    df1.to_csv('D:/Python Codes Lib/ASX operations/5_8.csv')
    
    df2=operate_8_13()
    df2.to_csv('D:/Python Codes Lib/ASX operations/8_13.csv')
    
    df3=operate_5_8_13()
    df3.to_csv('D:/Python Codes Lib/ASX operations/5_8_13.csv')
    
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    
def test():
    df1=operate_5_8()
    df1=df1[~df1['result'].str.contains('no enter')]
    df1=df1[~df1['result'].str.contains('no result')]
    df1.to_csv('D:/Python Codes Lib/5_8.csv')
    
    df2=operate_8_13()
    df2=df2[~df2['result'].str.contains('no enter')]
    df2=df2[~df2['result'].str.contains('no result')]
    df2.to_csv('D:/Python Codes Lib/8_13.csv')
    
    df3=operate_5_8_13()
    df3=df3[~df3['result'].str.contains('no enter')]
    df3=df3[~df3['result'].str.contains('no result')]
    df3.to_csv('D:/Python Codes Lib/5_8_13.csv')

    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    
if __name__ == '__main__':
    #test use test()
    test()

    #real operation use main()
    main()






