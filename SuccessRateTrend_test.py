# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


def new_column(file_name,m):
    path=r"D:\Python Codes Lib\ASX transcript"
    
    tr = '\\'
    
    df=pd.read_csv(path+tr+file_name+'.csv')

    df['Year&Month']=0
    
    df['target']=0
    
    for i in range(len(df)):
        if df['result'][i]=='stop loss':
            df['target'][i]=0
        else:
            df['target'][i]=1
            
    for i in range(len(df)):
        df['Year&Month'][i]=df['Date'][i][:7]
    
    list1=df['Year&Month'].tolist()
    
    list2=[]
    for i in range(len(list1)-1):
        if list1[i]!=list1[i+1]:
            list2.append(list1[i])
    
    #gain round number
    k=(len(list2)//m)*m
    
    d={}
    
    for i in range(0,k-m):
        d[list2[i]]=list2[i]
    
    for i in range(0,k-m,m):
        for v in range(1,m):
            d[list2[i+v]]=list2[i]
    
    list3=df['Year&Month'].tolist()
    
    list4=list(d.keys())
    
    target=list2[list2.index(list4[-1])+1]
    
    target_index=list3.index(target)
    
    df=df[:target_index][:]
    
    df['New_Year&Month']=0
    
    for i in range(len(df)):
        #try:
            df['New_Year&Month'][i]=d[df['Year&Month'][i]]
        #except:
            #KeyError
    
    
    df1=df.groupby(['New_Year&Month']).mean()
    df1.to_csv('D:/Python Codes Lib/1.csv')
    return df1

def main():
    new_column('ASX300_m=1',m=2)

if __name__ == '__main__':
    main()


