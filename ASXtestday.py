# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:42:12 2019

@author: XPS15
"""
import numpy as np
import datetime
import winsound

def CalculateDay(df):

    df=df[~df['result'].str.contains('stop loss')]

    df1=np.array(df)
    li3=df1.tolist()

    k=0
    
    for i in range(len(li3)):
        #date
        m=li3[i][1]
        year1=int(m[0:4])
        month1=int(m[5:7])
        day1=int(m[8:10])
    
        d1 = datetime.datetime(year1,month1,day1)
        
        #result
        n=li3[i][-3]
        year2=int(n[0:4])
        month2=int(n[5:7])
        day2=int(n[8:10])
    
        d2 = datetime.datetime(year2,month2,day2)
    
        m=d2-d1
        
        # k is accumulated total day
        k=k+m.days
    
    # k is the average day 
    k=k/len(li3)
    
    #程序结束，警报铃    
    return k


    


