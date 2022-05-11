#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: samanthapolanco
"""
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt


##reads the file surrounding state wise testing 
testing = pd.read_csv("StatewiseTestingDetails.csv")

##shows information regarding tsting in general and how many tests were negative or positive
##the results show that there were a total of 6969 negative resutls and a total of 5662 positive results

testing.info()

##sorts the number of testing activity perstate in chronological order which comes from the sort_values

testing.State.value_counts().sort_values()

##highest state with testing is haryana, I wanted to just point this out 

testing_Haryana = testing[testing.State=='Haryana']

##plotting the state with the highest activity surrounding rsting 

fig,ax1=plt.subplots()
##helps decide the size of the graphing data 

sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=testing_Haryana, ax=ax1)
ax1.set_title("Haryana data set ")
ax1.set_xlabel("date")
ax1.set_ylabel("Samples")
fig.tight_layout()
fig.savefig("highest testing data.png")

##state with the lowest testing data activity, wanted to compare this to the state 
##with the highest testing data, after sorting it, it was revealed that the testing with the 
##lowest testing data comprises of Dadra and Nagra Haveli and Damn and Diu

testing_Dadra = testing[testing.State=='Dadra and Nagar Haveli and Daman and Diu']

##plotting the data of the state with the lowest testing data 

fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=testing_Dadra, ax=ax1)
# this allows for the naming of the graph and both the x and y axes 
ax1.set_title("Dadra and Nagar Haveli and Daman and Diu")
ax1.set_xlabel("date")
ax1.set_ylabel("Samples")

## in order to make the graph more readable and an appropriate size one must utilize the tight_layout function 
fig.tight_layout()
fig.savefig("lowest testing data.png")











