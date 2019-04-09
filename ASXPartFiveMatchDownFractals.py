# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:58:08 2018

@author: XPS15
"""

#step 5 ASXPartFiveMatchDownFractals

import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASXPartTwoAveragerGluing import AveragerGluing_5_8
from ASXPartThreeFractals import DownFractal
import pandas as pd

#均线粘合的最低点
def AveragerGluingLowest(df,list):    
    dict={}
    for i in list:
        dict[i]=min(df['Low'][i],df['Low'][i+1],df['Low'][i+2])
    return dict

#匹配下分型
def MatchDownFractals(df,list1):
    #出现均线粘合的情况，keys为df中的位置，values是均线粘合三个中最高值
    dict1=AveragerGluingLowest(df,list1)
    
    #上分型，keys是df中的位置，values是最高值
    dict2=DownFractal(df)
    
    #开始匹配对应数值
    #list2 是对应的 均线粘合所在的df中的位置
    list2=list(dict1.keys())
    
    #list3下分型 在df里面的位置
    list3=list(dict2.keys())
    
    #有多少个粘合就有多少个与之配对的下分型
    list5=[0]*len(list2)
    
    for i in range(len(list2)):
        #每比较好一次，则更新一次list4
        list4=[]
        for k in list3:
            #保证下分型要低于均线粘合对应的三根K线的最高值
            if dict1[list2[i]]>dict2[k]:
                #当上分型的位置超过均线粘合的位置时候，则不选用
                if k>list2[i]:
                    continue
                #将均线粘合之前所有的下分型全部添加一起，取最后一个即为最近的下分型
                list4.append(k)
        
        #当list4存在时，则list4的最后一个分型，即为匹配分型       
        if len(list4) !=0:        
            list5[i]=list4[-1]
        #当list4不存在时，则用0来替代，后面会删除掉0的情况
        else:
            list5[i]=0
        
    return list5

def main(code):
    m=str(code)
    df=pd.read_csv('D:/Python Codes Lib/ASX database/'+m+'.csv')
    list1=AveragerGluing_5_8(df)
    list2=MatchDownFractals(df,list1)
    return list2

if __name__ == '__main__':
    main('ANZ')