# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:21:59 2019

@author: RITIKA MANDAL
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets
data,target = datasets.load_iris(return_X_y=True) 

df={}
d=[]

#Importing data
dataset=pd.read_csv('C:/Users/RITIKA MANDAL/documents/projects/series.csv')
#Printing head
dataset.head()

for i in dataset['HOUSE_NAME'].unique():
    d.append(i)

m=0
i=0    

while(i<len(d)):
    n=0
    for j in range(m,600):
        if(dataset.iloc[j,0]==d[i]):
            df[i]=pd.DataFrame(dataset.iloc[j-n:j+0,:])
            n=n+1
            m=m+1
    i=i+1

for i in range(len(df)):

      train=df[i][0:20] 
      test=df[i][20:]
      df[i].Timestamp = pd.to_datetime(df[i].DATE,format='%d-%m-%Y') 
      df[i].index = df[i].Timestamp 
      df[i] = df[i].resample('D').mean()
      train.Timestamp = pd.to_datetime(train.DATE,format='%d-%m-%Y') 
      train.index = train.Timestamp 
      train = train.resample('D').mean() 
      test.Timestamp = pd.to_datetime(test.DATE,format='%d-%m-%Y') 
      test.index = test.Timestamp 
      test = test.resample('D').mean()
      
      train.ELECTRICITY_CONSUMPTION.plot(figsize=(15,8), title= 'ELECTRICITY_CONSUMPTION', fontsize=14)
      test.ELECTRICITY_CONSUMPTION.plot(figsize=(15,8), title= 'ELECTRICITY_CONSUMPTION', fontsize=14)
      plt.show() 