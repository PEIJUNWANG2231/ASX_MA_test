# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:39:24 2019

@author: XPS15
"""

# if use the script, the result only remain date and stop loss
import pandas as pd
import os
import re

path = r'D:\Python Codes Lib\ASX transcript'

def get_file():                   
    # read the file in local pc
    files =os.listdir(path)
    files.sort() 
    
    #create an empty list
    list= []
    for file in files:
        if not  os.path.isdir(path +file):  #判断该文件是否是一个文件夹       
            f_name = str(file)        
            #print(f_name)
            tr = '\\'   #多增加一个斜杠
            filename = path + tr + f_name        
            list.append(filename)  
    return list

def read_csv(path):
    df=pd.read_csv(path)
    return df

# m: para mutiplies the difference of Enter and StopLoss
# m is depended on the names of file. such as ASX300_m=1
def rearrage_cols(df,m):  
    # in this step, the value of m should be notice
    # n is commission charge
    n=0.001*2
    
    #create two new columns:return & accumulated return
    #type:float
    df['return']=0.0
    df['accumulated return']=0.0
    
    #rearrage the dataframe
    df=df[['Date','code','Open','High','Low',
           'Close','type','Enter','StopLoss',
           'StopLossPct','result','return',
           'accumulated return']]
    
    #Sort Pandas Dataframe by Date;then, reindex.
    df['Date'] =pd.to_datetime(df['Date'])
    
    df=df.sort_values(by=['Date']).reset_index(drop=True)
    
    #judge result is stop loss or not?
    # m: para mutiplies the difference of Enter and StopLoss
    # m is depended on the names of file. such as ASX300_m=1
    for i in range(len(df)):
        if df['result'][i]=='stop loss':
            df['return'][i]=1-df['StopLossPct'][i]*m-n
        else:
            df['return'][i]=1+df['StopLossPct'][i]*m-n
    
    #calculate accumulated return
    df['accumulated return'][0]=df['return'][0]
    
    for i in range(1,len(df)):
        a=df['accumulated return'][i-1]
        df['accumulated return'][i]=a*df['return'][i]
    return df


def main():
    list1=get_file()
    
    list2=[]
    for i in list1:   
        numbers=re.findall(r"\d+\.?\d*",i)
        m=float(numbers[-1])
        list2.append(m)
    
    for i in range(len(list1)):
        df1=read_csv(list1[i])
        df2=rearrage_cols(df1,list2[i])
        df2.to_csv(list1[i])
          
if __name__ == '__main__':
    main()
    



    
    

    
    
    
    
    