# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:34:08 2018

@author: XPS15
"""
import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASXPartThreeFractals import UpFractal, DownFractal

#微调所有上分型，变为进场价格
def EnterPoint(df):
    dict1=UpFractal(df)
    
    list1=list(dict1.keys())
    
    for i in list1:
        if dict1[i]*100%5==0:
            dict1[i]=dict1[i]+0.01
        else:
            dict1[i]=((int(dict1[i]*100/5)+1)*5+1)/100
    return dict1

#微调所有下分型，变为止损价格
def StopLossPoint(df):
    dict1=DownFractal(df)
    
    list1=list(dict1.keys())
    
    for i in list1:
        if dict1[i]*100%5==0:
            dict1[i]=dict1[i]-0.01
        else:
            dict1[i]=(int(dict1[i]*100/5)*5-1)/100
    return dict1


   


 




