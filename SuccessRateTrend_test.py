# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# to gain the success rate  of trading system
import pandas as pd
import datetime

def get_month_range(start_day,end_day):
  months = (end_day.year - start_day.year)*12 + end_day.month - start_day.month
  month_range = ['%s-%s'%(start_day.year + mon//12,mon%12+1) 
                    for mon in range(start_day.month-1,start_day.month + months)]
  list2=month_range
  
  for i in range(len(list2)):
        if len(list2[i])!=7:
            list2[i]=list2[i][:5]+'0'+list2[i][5:]
  
  return list2


def new_column(file_name,m):
    path="D:/Python Codes Lib/ASX transcript"
    
    tr = '/'
    
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
    
    #引入日期函数
    last_day=str(df['Date'][len(df)-1:])
    
    year=int(last_day[8:12])
    month=int(last_day[13:15])

    list2=get_month_range(datetime.date(2000, 1, 1),datetime.date(year,month,1))
    
    #gain round number
    k=(len(list2)//m)*m
    
    d={}
    
    #先填充list2的元素
    for i in range(0,k-m):
        d[list2[i]]=list2[i]
    
    #类聚，m个为一组
    for i in range(0,k-m,m):
        for v in range(1,m):
            d[list2[i+v]]=list2[i]
    
    list3=df['Year&Month'].tolist()
    
    list4=list(d.keys())
    
    #调整df 长度
    #到list4的最后一个元素
    target=list2[list2.index(list4[-1])+1]
    
    target_index=list3.index(target)
    
    df=df[:target_index][:]
    
    #用字典的方式嵌套进去
    df['New_Year&Month']=0
    
    for i in range(len(df)):
        #try:
            df['New_Year&Month'][i]=d[df['Year&Month'][i]]
        #except:
            #KeyError
    
    
    df1=df.groupby(['New_Year&Month']).mean()
    
    df1=df1.loc[:, ['target']]
    
    path='D:/Python Codes Lib/'+file_name+'_month'+str(m)+'_SuccessRate.csv'
    df1.to_csv(path)
    return df1

def main():
    new_column('5_8_m=1',m=4)
    new_column('5_8_13_m=1',m=4)
    new_column('8_13_m=1',m=4)
    
if __name__ == '__main__':
    main()