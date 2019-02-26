# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:09:15 2019

@author: XPS15
"""
import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASXPartTwoAveragerGluing import AveragerGluing
from ASXPartFourMatchUpFractals import MatchUpFractals
from ASXPartFiveMatchDownFractals import MatchDownFractals
from ASXPartSixEnterAndLossPoint import EnterPoint,StopLossPoint
import numpy as np
import pandas as pd

#遍历所有均线粘合的情况，并得出对应的结果
def IterAveragerGluing(df):
    #剔除掉没有上分型和下分型的情况
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
        del li1[i]
        del li2[i]
        

    dict1=EnterPoint(df)
    
    dict2=StopLossPoint(df)
    
    #将dataframe变成list，每个元素对应一行
    df1=np.array(df)
    li3=df1.tolist()
    
    list2=[]
    
    for i in range(len(list1)):
        list3=[]
        for n in range(len(li3)):
            
            if list1[i]>n:
                continue
            
            if n> list1[i]+20:
                continue
            
            #当StopLoss Point 大于 enter point 则错误
            if dict2[li2[i]]>=dict1[li1[i]]:
                continue
            
            #low:3，li3[n][3]
            #当最低价低于StopLossPoint时，则不操作
            if li3[n][3] < dict2[li2[i]]:
                continue
            
            #high:2,li3[n][2]
            if li3[n][2] >= dict1[li1[i]]:
                list3.append(n)
        
        #如何没有进场，则添加0表示      
        if len(list3) ==0:
            list2.append(0)
        else:
            list2.append(list3[0])
    
    list5=[]
    for i in range(len(list2)):
        
        list4=[]

        for n in range(len(li3)):
            if list2[i]==0:
                list4.append('no enter')

            else:
                if list2[i]>n:
                    continue
                
                #low:3，li3[n][3]
                if li3[n][3]<dict2[li2[i]]:
                    list4.append('stop loss')
                
                m=(dict1[li1[i]]-dict2[li2[i]])
                
                #high:2,li[n][2]
                if li3[n][2]>1*m+dict1[li1[i]]:
                    list4.append(df['Date'][n])
                
            
            if len(list4)==1:
                break
        
        if len(list4)==0:
            list5.append('no result')
        else:
            list5.append(list4[0])
    return list5

def main(code):
    m=str(code)
    df=pd.read_csv('D:/Python Codes Lib/ASX database/'+m+'.csv')
    list1=AveragerGluing(df)
    for i in list1:
        print('Date of AveragerGluing is',df['Date'][i])

    list2=IterAveragerGluing(df)
    return list2

if __name__ == '__main__':
    main('ANZ')            
                    
            
                        
                
                    
                
                
        
    
    


