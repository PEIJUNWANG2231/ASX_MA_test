# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# to gain the success rate  of trading system
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
    path='D:/Python Codes Lib/'+file_name+'_month'+str(m)+'_SuccessRate.csv'
    df1.to_csv(path)
    return df1

def main():
    new_column('5_8_m=1',m=12)
    new_column('5_8_13_m=1',m=12)
    new_column('8_13_m=1',m=12)
    
if __name__ == '__main__':
    main()


