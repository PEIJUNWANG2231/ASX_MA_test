# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:03:11 2019

@author: XPS15
"""
import pandas as pd
import sys
sys.path.append(r'D:\Python Codes Lib\ASX list of code')
from ASX_Standized_CSV import get_file
from ASXtestday import CalculateDay
from pandas.core.frame import DataFrame

#numbers of deals
def total_deals(df):
    total_deals=len(df)
    return total_deals

#sussecc rate
def SuccessRate(df):
    df1=df[~df['result'].str.contains('stop loss')]    
    SR=len(df1)/len(df)
    return SR
    
#max_loss 
def Max_Loss(df):
    list1=df['return'].tolist()
    MaxLoss=min(list1)-1
    return MaxLoss

#max_profit
def Max_Profit(df):
    list1=df['return'].tolist()
    MaxProfit=max(list1)-1
    return MaxProfit

#continuous_profit
def Continous_Profit(df):
    global Start1
    global End1
    
    list1=df['return'].tolist()

    list2=[]
    for i in list1:
        if i >=1:
            list2.append(1)
        else:
            list2.append(0)
    
    # seek 1,0 combination
    list3=[]
    for i in range(len(list2)-1):
        if list2[i]==1:
            if list2[i]!=list2[i+1]:
                list3.append(i)
    
    #seek 0,1 combination
    list4=[]
    for i in range(len(list2)-1):
        if list2[i]==0:
            if list2[i]!=list2[i+1]:
                list4.append(i)
    
    #the target list should be 0111110.
    list5=[]
    
    #dictionary response to: 10:01
    d={}
    
    for i in list3:
        for k in list4:
            if i<k:
                continue
            else:
                list5.append(k)
        
        if len(list5) !=0:        
            d[i]=list5[-1]
    
    #list6 对应的是10的位置
    list6=list(d.keys())
    
    #list7 对应的是01的位置
    list7=list(d.values())
    
    list8=[]
    for i in range(len(list6)):
        m=list6[i]-list7[i]
        list8.append(m)
    
    Continous_Profit=max(list8)
    
    index=list8.index(Continous_Profit)
    
    Start1=df['Date'][list7[index]]
    
    End1=df['Date'][list6[index]]
    
    return Continous_Profit     
    
    
#continuous_loss
def Continous_Loss(df):
    global Start2    
    global End2
    
    list1=df['return'].tolist()

    list2=[]
    for i in list1:
        if i >=1:
            list2.append(1)
        else:
            list2.append(0)
  
    # seek 1,0 combination
    list3=[]
    for i in range(len(list2)-1):
        if list2[i]==1:
            if list2[i]!=list2[i+1]:
                list3.append(i)
    
    #seek 0,1 combination
    list4=[]
    for i in range(len(list2)-1):
        if list2[i]==0:
            if list2[i]!=list2[i+1]:
                list4.append(i)
    
    #the target list should be 1000001.
    list5=[]
    
    #dictionary response to: 
    d={}
    
    for i in list4:
        for k in list3:
            if i<k:
                continue
            else:
                list5.append(k)
        
        if len(list5)!=0:        
            d[i]=list5[-1]
    
    #list6 对应的是01的位置
    list6=list(d.keys())
    
    #list7 对应的是10的位置
    list7=list(d.values())
    
    list8=[]
    for i in range(len(list6)):
        m=list6[i]-list7[i]
        list8.append(m)
    
    Continuous_Loss=max(list8)
    
    index=list8.index(max(list8))
    
    Start2=df['Date'][list7[index]]
    
    End2=df['Date'][list6[index]]
    
    return Continuous_Loss

#AverageReturn
def AverageReturn(df):
    list1=df['return'].tolist()
    
    s=1
    for i in list1:
        s *=i
    
    AverageReturn=s**(1/len(df))-1
    
    if type(AverageReturn) is complex:
        AverageReturn='the value is noe existing'    
    return AverageReturn

#effective average return
def Eff_Annual_Return(df):
    day=CalculateDay(df)
    AR=AverageReturn(df)
    
    if type(AR) is str:
        Eff_Annual_Return='the value is noe existing'
    else:
        AR=AR+1
        Eff_Annual_Return=(AR**(1/day))**365-1
    return Eff_Annual_Return

def main():
    list1=get_file()
    
    name=[]
    num_of_trading=[]
    success_rate=[]
    max_profit=[]
    max_loss=[]
    continous_profit=[]
    start1=[]
    end1=[]
    continous_loss=[]
    start2=[]
    end2=[]
    lasting_aver_day=[]
    averagereturn=[]
    effective_annual_return=[]
    
    for i in list1:
        name.append(i[35:])
        df=pd.read_csv(i)
        num_of_trading.append(total_deals(df))
        success_rate.append(SuccessRate(df))
        max_loss.append(Max_Loss(df))
        max_profit.append(Max_Profit(df))
        continous_profit.append(Continous_Profit(df))
        start1.append(Start1)
        end1.append(End1)
        continous_loss.append(Continous_Loss(df))
        start2.append(Start2)
        end2.append(End2)
        lasting_aver_day.append(CalculateDay(df))
        averagereturn.append(AverageReturn(df))
        effective_annual_return.append(Eff_Annual_Return(df))
    
    df={'name': name,
    'num_of_trading':num_of_trading,
    'success_rate': success_rate,
    'max_profit': max_profit,
    'max_loss':max_loss,
    'continous_profit':continous_profit,
    'start1':start1,
    'end1':end1,
    'continous_loss':continous_loss,
    'start2':start2,
    'end2':end2,
    'lasting_aver_day':lasting_aver_day,
    'averagereturn':averagereturn,
    'effective_annual_return':effective_annual_return}
    
    dataframe=DataFrame(df)
    
    dataframe.to_csv('D:/Python Codes Lib/ASX_Result_analysis.csv')
        
    return dataframe

if __name__ == '__main__':
    main()
        
        
   
    
    