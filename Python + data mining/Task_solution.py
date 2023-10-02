#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:54:58 2023

@author: nazokatakhmadjonova
"""

import pandas as pd
import numpy as np

file = "//Users//nazokatakhmadjonova//Desktop//Big Data in Business and Industry //Python + data mining//AB_NYC_2019.csv"
df = pd.read_csv(file)

#%% TASK1 
#(A)
df2=df.loc[df['neighbourhood'] == "Clifton"] # filter by the row neighbourhood where the value is "Clifton"
grp = df2.groupby('neighbourhood')["price"].mean() #

#%%
#(B)
df3=df.loc[df['neighbourhood'] == "Harlem"] # filter by the row neighbourhood where the value is "Harlem"
grp2 = df3.groupby(['neighbourhood','room_type'])["id"].count() #

#%%
#(C)
df4=df3.loc[df['room_type']=="Private room"]
grp3 = df4.groupby("host_id")["id"].count()#
grp4 = grp3[grp3>1].count()

#%% TASK2
#(A)
def filter_func(nh, max_pr, r_type):
    filtered_d = df.copy()
    filtered_d= filtered_d.loc[filtered_d["neighbourhood"]==nh]
    filtered_d= filtered_d.loc[filtered_d["price"]<=max_pr]
    filtered_d= filtered_d.loc[filtered_d["room_type"]==r_type]
    return filtered_d
filter_result = filter_func('Clifton',50,'Private room')

print(filter_result)

#%%
#(B)
def filter_func2(nh, max_pr, r_type):
    filtered_d2 = df.copy()
    filtered_d2= filtered_d2.loc[filtered_d2["neighbourhood"]==nh]
    filtered_d2= filtered_d2.loc[filtered_d2["price"]<=max_pr]
    filtered_d2= filtered_d2.loc[filtered_d2["room_type"]==r_type]
    
    if filtered_d2.empty:
        return "No matching results"
    
    print("Ten cheapest alternatives:")
    cheapest_alternatives = filtered_d2.sort_values(by='price').head(10)[['host_name', 'neighbourhood', 'price', 'minimum_nights']]
   
        
    return cheapest_alternatives

filter_result = filter_func2('Clifton',30,'Private room')

print(filter_result)

#%% TASK3

df5= df.loc[df['room_type']=='Entire home/apt']
grouped_data = df5.groupby("neighbourhood")
summary_table = pd.DataFrame({
        'Average price': grouped_data['price'].mean(),
        'Number of places': grouped_data.size(),
        'Number of hosts': grouped_data['host_id'].nunique()
    })
summary_table = summary_table[summary_table['Number of places'] >= 5]

summary_table['Places per Host Ratio'] = summary_table['Number of places'] / summary_table['Number of hosts']
    

#(A) Which neighbourhood is the most expensive one? Provide price.
most_expensive_ngbh = summary_table['Average price'].idxmax()
most_expensive_price = summary_table.loc[most_expensive_ngbh, 'Average price']

#(B) Which neighbourhood has the highest [Number of places]/[Number of hosts] -ratio?
# Provide value of the ratio.
highest_ratio_ngbh = summary_table['Places per Host Ratio'].idxmax()
highest_ratio_val= summary_table.loc[highest_ratio_ngbh, 'Places per Host Ratio']


#Print the answers:
print("Most Expensive Neighborhood:", most_expensive_ngbh)
print("Price in the Most Expensive Neighborhood:", most_expensive_price)
print("Neighborhood with the Highest [Number of places]/[Number of hosts] Ratio:", highest_ratio_ngbh)
print("Value of the Highest Ratio:", highest_ratio_val)

print(summary_table)



