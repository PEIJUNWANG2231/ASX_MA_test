# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:33:20 2018

@author: XPS15
"""
import datetime
import pandas as pd
import numpy as np

def UpFractal(df):
#2.1 上分型 
    df1=np.array(df)
    li=df1.tolist()
    
    list1=[]
    #high:2
    for i in range(2, len(li)-2):
        if li[i-2][2]<li[i][2]:
            if li[i-1][2]<li[i][2]:
                if li[i+1][2]<li[i][2]:
                    if li[i+2][2]<li[i][2]:
                        list1.append(i)

    dict={}
    for i in list1:
        dict[i]=li[i][2]
    return dict
    

def DownFractal(df):
##2.2 下分型                    
    list2=[]
    df1=np.array(df)
    li=df1.tolist()
    
    #low:3
    for i in range(2, len(li)-2):
        if li[i-2][3]>li[i][3]:
            if li[i-1][3]>li[i][3]:
                if li[i+1][3]>li[i][3]:
                    if li[i+2][3]>li[i][3]:
                        list2.append(i)
    dict={}
    for i in list2:
        dict[i]=li[i][3]
    return dict

def main(code):
    start = datetime.datetime.now()
    df=pd.read_csv('D:/Python Codes Lib/ASX database/'+code+'.csv')
    UpFractal(df)
    DownFractal(df)
    end = datetime.datetime.now()
    print(end-start)
    
if __name__ == '__main__':
    main('AAC')
