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
t1a=df[df.neighbourhood == "Clifton"]["price"].mean() # 
print("The mean price in Clifton neighbourhood:",t1a)

#-----------
#df2=df.loc[df['neighbourhood'] == "Clifton"] # filter by the row neighbourhood where the value is "Clifton"
#grp = df2.groupby('neighbourhood')["price"].mean() #

#%%
#(B)
t1b=df[(df.neighbourhood == "Harlem") & (df.room_type=="Private room")]["id"].count() 
print("There are ", t1b, " private rooms in Harlem")

#----------
#df3=df.loc[df['neighbourhood'] == "Harlem"] # filter by the row neighbourhood where the value is "Harlem"
#grp2 = df3.groupby(['neighbourhood','room_type'])["id"].count() #

#%%
#(C)
t1c=df[(df.neighbourhood == "Harlem") & (df.room_type=="Private room")].groupby("host_id")["host_id"].count()
t1c = t1c[t1c>1].count()
print(t1c," hosts in Harlem have more than 1 private room")

#----------
#df4=df3.loc[df['room_type']=="Private room"]
#grp3 = df4.groupby("host_id")["id"].count()#
#grp4 = grp3[grp3>1].count()

#%% TASK2
#(A)
def filter_func(nh, max_pr, r_type):
    filtered_d = df.copy()
    #filter the values in neigbourhood column with the user given parameter on nh checking when the first is equal to the second
    #save the result in filtered_d
    filtered_d= filtered_d.loc[filtered_d["neighbourhood"]==nh]
    #filter the values in price column with the user given parameter on max_pr when price is less then or eqaul max_pr
    #update the variable in filtered_d2
    filtered_d= filtered_d.loc[filtered_d["price"]<=max_pr]
    #filter the values in room_type column with the user given parameter on r_type when the first is equal to the second
    #update the variable in filtered_d2
    filtered_d= filtered_d.loc[filtered_d["room_type"]==r_type]
    return filtered_d
filter_result = filter_func('Clifton',50,'Private room')

print(filter_result)

#%%
#(B)
def filter_func2(nh, max_pr, r_type):
    filtered_d2 = df.copy()
    #filter the values in neigbourhood column with the user given parameter on nh checking when the first is equal to the second
    #save the result in filtered_d2
    filtered_d2= filtered_d2.loc[filtered_d2["neighbourhood"]==nh] 
    #filter the values in price column with the user given parameter on max_pr when price is less then or eqaul max_pr
    #update the variable in filtered_d2
    filtered_d2= filtered_d2.loc[filtered_d2["price"]<=max_pr]
    #filter the values in room_type column with the user given parameter on r_type when the first is equal to the second
    #update the variable in filtered_d2
    filtered_d2= filtered_d2.loc[filtered_d2["room_type"]==r_type]
    
    #if after filtering the dataframe is empty then print "No matching results" message
    if filtered_d2.empty:
        return "No matching results"
    
    #in other case print the message "Ten cheapest alternatives:" and return the fully filtered dataframe with 10 cheapest alternatives
    print("Ten cheapest alternatives:")
    cheapest_alternatives = filtered_d2.sort_values(by='price').head(10)[['host_name', 'neighbourhood', 'price', 'minimum_nights']]
    return cheapest_alternatives

#calling the funtion for the check
filter_result = filter_func2('Clifton',30,'Private room')
#print the result of the function
print(filter_result)

#%% TASK3
#filter the room_type - "Entire home/apt"
df5= df.loc[df['room_type']=='Entire home/apt']
#group data by the "neighbourhood"
grouped_data = df5.groupby("neighbourhood")
#create a summary table dataframe 
summary_table = pd.DataFrame({
    #create the column named "Average price" which contains calculated average of the grouped data 
        'Average price': grouped_data['price'].mean(), 
    #create the column named "Number of places" which contains the count of the grouped data         
        'Number of places': grouped_data.size(),
    #create the column named "Number the columns" which contains counts the unique host_ids
        'Number of hosts': grouped_data['host_id'].nunique()
    })
#Include neighbourhoods with five or more places
summary_table = summary_table[summary_table['Number of places'] >= 5]
#save the copy of summary table that will be printed in a new variable summary_table1 to be able to do the manipulations for further calculations with the summary_table
summary_table1 = summary_table.copy()
#new calculted column for [Number of places]/[Number of hosts] -ratio
summary_table['Places per Host Ratio'] = summary_table['Number of places'] / summary_table['Number of hosts']
    

#(A) Which neighbourhood is the most expensive one? Provide price.
most_expensive_ngbh = summary_table['Average price'].idxmax()
most_expensive_price = summary_table.loc[most_expensive_ngbh, 'Average price']

#(B) Which neighbourhood has the highest [Number of places]/[Number of hosts] -ratio?
# Provide value of the ratio.
highest_ratio_ngbh = summary_table['Places per Host Ratio'].idxmax()
highest_ratio_val= summary_table.loc[highest_ratio_ngbh, 'Places per Host Ratio']

#print the summary_table\
    
print(summary_table1)

#Print the answers:
print("Most Expensive Neighborhood:", most_expensive_ngbh)
print("Price in the Most Expensive Neighborhood:", most_expensive_price)
print("Neighborhood with the Highest [Number of places]/[Number of hosts] Ratio:", highest_ratio_ngbh)
print("Value of the Highest Ratio:", highest_ratio_val)
