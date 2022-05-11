#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:18:42 2022

@author: samanthapolanco
"""

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

covid = pd.read_csv("covid_19_india.csv")
vaccine_status = pd.read_csv("covid_vaccine_statewise.csv")
testing = pd.read_csv("StatewiseTestingDetails.csv")

#check if there are null values

covid.info()

# Dropping the columns

covid.drop(columns=["Sno",'Time',],inplace=True)

#Grouping and summing the cases

covidcc=covid.groupby(["Date","State/UnionTerritory"], as_index=False).sum()
print(covidcc)

#In order to get the values sorted and cleaned, we going to combine all cases (Cured, Deaths) together

covid_cases = covid.groupby(['State/UnionTerritory'])['Cured','Deaths','Confirmed'].sum().reset_index()
covid_nation=covid[['State/UnionTerritory','ConfirmedIndianNational','ConfirmedForeignNational']]

#Getting rid of null values: 

covid_nation.isnull().sum()
covid_nation.dtypes

#Sorting the data types under the same one, so that it would be easier to work with them

covid_nation['ConfirmedIndianNational'] = covid_nation['ConfirmedIndianNational'].replace('-',0)
covid_nation['ConfirmedForeignNational'] = covid_nation['ConfirmedForeignNational'].replace('-',0)
covid_nation['ConfirmedIndianNational'] = covid_nation['ConfirmedIndianNational'].astype('int64')
covid_nation['ConfirmedForeignNational']= covid_nation['ConfirmedForeignNational'].astype('int64')
covid_nation.dtypes

covid_cleaned = covid_nation.groupby(['State/UnionTerritory'])['ConfirmedIndianNational','ConfirmedForeignNational'].sum().reset_index()
covid_sort_cleaned = covid_cleaned.sort_values(by='ConfirmedIndianNational',ascending=False).reset_index(drop=True)
covid_sort_cleaned.head(10)

#these sets of code set up graphing

fig, ax1=plt.subplots()
sns.set(rc={'figure.figsize':(17,6)})
cases=sns.barplot(data=covid_sort_cleaned[:10],x='State/UnionTerritory',y='ConfirmedIndianNational').set(title="Covid Cases by Territory")
fig.tight_layout()
fig.savefig("Cases among Indians by Territory.png")

#Now the same graph just for cases among internationals in India by territory

covid_sort_international = covid_cleaned.sort_values(by='ConfirmedForeignNational',ascending=False).reset_index(drop=True)
fig, ax1=plt.subplots()
sns.set(rc={'figure.figsize':(17,6)})
cases=sns.barplot(data=covid_sort_international[:10],x='State/UnionTerritory',y='ConfirmedForeignNational').set(title="Covid Cases among Foreign-Born by Territory")
fig.tight_layout()
fig.savefig("Cases among Foreign Born by Territory.png")

#Looking at each state and each type of the cases and seeing the correlations

# this also shows the results of the confirmed covid cases 

fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(10,6)})
confirmed = sns.barplot(data=covid_cases,x=covid_cases.index,y=covid_cases["Confirmed"])

##this helps set up the x  axis properly and easy to identify, in this scenario 
##the x label is territory is saved territory why the the title is total confirmed taxes 

ax1.set_title("Total Confirmed Cases")
ax1.set_xlabel("Territory")
fig.tight_layout()
fig.savefig("Confirmed Cases.png")

#this shows the reults for the cured cases similarly in the same way 

fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(10,6)})
cured = sns.barplot(data=covid_cases,x=covid_cases.index,y=covid_cases["Cured"])
ax1.set_title("Total Cured Cases")
ax1.set_xlabel("Territory")
fig.tight_layout()
fig.savefig("Cured Cases.png")

#this shows the results for deaths caused by covid 

fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(10,6)})
deaths = sns.barplot(data=covid_cases,x=covid_cases.index,y=covid_cases["Deaths"])
ax1.set_title("Total Deaths Cases")
ax1.set_xlabel("Territory")
fig.tight_layout()
fig.savefig("Deaths.png")






