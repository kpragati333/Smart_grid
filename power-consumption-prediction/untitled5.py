# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:56:39 2019

@author: RITIKA MANDAL
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os
from sklearn import metrics


dataset=pd.read_csv('C:/Users/RITIKA MANDAL/documents/projects/ele.csv')
x=dataset.iloc[:,1].values
y=dataset.iloc[:,2].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

x_train=x_train.reshape(-1,1)
y_train=y_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)
y_test=y_test.reshape(-1,1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression() 
regressor.fit(x_test, y_test)

y_pred=regressor.predict(x_test)
from sklearn.metrics import mean_squared_error
from math import sqrt
mse=round((mean_squared_error(y_test,y_pred))/100, 2)
rmse = round((sqrt(mse))/100 ,2)

y_pred=regressor.predict(x_test)



def viz_linear():
    plt.scatter(x_test, y_test, color='red')
    plt.plot(x_test, y_pred, color='blue')
    plt.title('ELECTRICITY CONSUMPTION')
    plt.xlabel('WEEK_DAY')
    plt.ylabel('ELECTRICITY_CONSUMPTION')
    plt.show()
    return
viz_linear()


    
example_pivot=dataset.pivot_table(index="WEEK_DAY", columns="HOUSE_NAME", values="ELECTRICITY_CONSUMPTION")   
print(example_pivot)
example_pivot.plot(kind='bar',width=0.8,figsize=(20,12))

print(mse)



