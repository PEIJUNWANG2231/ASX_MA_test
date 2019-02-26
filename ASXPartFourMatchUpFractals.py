# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:01:28 2018

@author: XPS15
"""
import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASXPartTwoAveragerGluing import AveragerGluing
from ASXPartThreeFractals import UpFractal
import pandas as pd
import datetime

#均线粘合的最高点
def AveragerGluingHighest(df,list):    
    dict={}
    for i in list:
        dict[i]=max(df['High'][i],df['High'][i+1],df['High'][i+2])
    return dict

#匹配上分型
def MatchUpFractals(df,list1):
    #出现均线粘合的情况，keys为df中的位置，values是均线粘合三个中最高值
    dict1=AveragerGluingHighest(df,list1)
    
    #上分型，keys是df中的位置，values是最高值
    dict2=UpFractal(df)
    
    #开始匹配对应数值
    list2=list(dict1.keys())
    
    list3=list(dict2.keys())
    
    list4=[]
    
    list5=[0]*len(list2)
    
    for i in range(len(list2)):
        for k in list3:
            if dict1[list2[i]]<dict2[k]:
                if k>list2[i]:
                    continue
                list4.append(k)
        
        if len(list4) !=0:        
            list5[i]=list4[-1]
        else:
            list5[i]=0
        
    return list5

def main(code):
    start = datetime.datetime.now()
    m=str(code)
    df=pd.read_csv('D:/Python Codes Lib/ASX database/'+m+'.csv')
    list1=AveragerGluing(df)
    list2=MatchUpFractals(df,list1)
    end = datetime.datetime.now()
    print(end-start)
    return list2

if __name__ == '__main__':
    main('AAC')




