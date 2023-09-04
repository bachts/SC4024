# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:17:07 2021

CZ4124 Data Visualisation (Tutorial 1 Template)
@author: Put your name here
 
"""

import matplotlib.pyplot as plt
import pandas as pd

PlotWithPandas = False  # you can plot either with Pandas or Matplotlib
#---------------------------------------------------------------------
# Read in Daily Temperature datafile into dataframe Temp
#---------------------------------------------------------------------
Temp = pd.read_csv('Daily_Temperature.csv')  # change to your directory
# print('\nTable read in\n',Temp,'\n')

#---------------------------------------------------------------------
# Use MELT to covert to long form and apply column names
#---------------------------------------------------------------------
# put in your code here
melt_df = Temp.melt(id_vars=['Name']) #id stay the same, but now the columns are turn into variables, with a standalone value column
# print(melt_df)
    
#---------------------------------------------------------------------
# Use PIVOT to convert to wide form with Names in each column
#---------------------------------------------------------------------
# put in your code here
pivot_df = melt_df.pivot(index='variable', columns='Name') # take long form and pivot around index, columns taking index from melt
# print(pivot_df)

#-------------------------------
# Use Pandas to plot line chart
#-------------------------------

print(pivot_df)
temp1 = pd.read_csv('Temp_Week_1.csv')
temp2 = pd.read_csv('Temp_Week_2.csv')
temp1.fillna(temp1['Temp'].mean(), inplace=True)
temp2.fillna(temp2['Temp'].mean(), inplace=True)

merge_df = pd.concat([temp1, temp2]) #axis = 0: vertically, axis=1: horizontally
merge_df['Day'] = merge_df['Day'] + merge_df['Week']

if(PlotWithPandas):
    print('\nPlotting with Pandas')
    # put your Pandas plotting code here

    
#----------------------------------
# Use Matplotlib to plot line chart
#----------------------------------
else:  
    print('\nPlotting with Matplotlib')
    # Alternatively, you can do the plot using Matplotlib or 
    # any other Python plotting library
    plt.subplot(1, 2, 1)
    plt.plot(temp1['Day'], temp1['Temp'], label='Week 1')
    plt.plot(temp2['Day'], temp2['Temp'], label='Week 2')
    plt.title('Average Daily Temperature Changes')
    plt.xlabel('Day of week')
    plt.ylabel('Temperature(Celsius)')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(merge_df['Day'], merge_df['Temp'])
    plt.show()  