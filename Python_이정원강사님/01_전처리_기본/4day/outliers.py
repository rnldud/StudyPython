#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np

def outliers_iqr3(dframe, data): 
    #q1, q3 값 확인하기
    #percentile(): 25%와 75% 시점의 데이터 값을 알려줌(return)
    q1,q3 = np.percentile(data,[25, 75]) 
    print(q1) 
    print(q3) 
    
    #iqr 값 계산
    iqr = q3-q1   
    print(iqr)
    
    #최대값 계산
    upper_bound = q3 + (iqr * 1.5)
    print(upper_bound)
    
    #최소값 계산
    lower_bound = q1 - (iqr * 1.5)
    print(lower_bound)
    
    #나이 데이터에서 이상치 값 조회하기 
    df_temp = dframe[(data> upper_bound) | 
                     (data< lower_bound)] #전체 조회위해 data로 변경 
    print(len(df_temp))
    print(df_temp)

