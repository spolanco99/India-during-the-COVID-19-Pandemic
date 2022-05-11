
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:13:15 2022

@author: samanthapolanco
"""

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

##opens and reads the file on hand in this case its the activity surrounding vaccination status/demographics 
vaccine_status = pd.read_csv("covid_vaccine_statewise.csv")

## this sets up a graph to show the activity surrounding vaccination in different 
##demographics starting with females within India 
fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=vaccine_status["Female(Individuals Vaccinated)"], ax=ax1)
ax1.set_title("Female(Individuals Vaccinated)")
ax1.set_xlabel("vaccine status")
ax1.set_ylabel("Female(Individuals Vaccinated)")
fig.tight_layout()
fig.savefig("Female(Individuals Vaccinated).png")

# this sets up a graph to show the activity surrounding vaccination in different 
##demographics similarly to the function above but this analyzes vaccination activity 
#but among males
fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=vaccine_status["Male(Individuals Vaccinated)"], ax=ax1)
ax1.set_title("Male(Individuals Vaccinated)")
ax1.set_xlabel("vaccine status")
ax1.set_ylabel("Male(Individuals Vaccinated)")
fig.tight_layout()
fig.savefig("Male(Individuals Vaccinated).png")

## this is meant to highlight the number of people who at least recieved one dose of the vaccine and the level that it was occuring at 

fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=vaccine_status["First Dose Administered"], ax=ax1)
ax1.set_title("First Dose Administered,")
ax1.set_xlabel("number of people")
ax1.set_ylabel("First Dose Administered,")
fig.tight_layout()
fig.savefig("First Dose Administered.png")

##this analyzes the number of people who opted in getting the second dose of the vaccine

fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=vaccine_status["Second Dose Administered"], ax=ax1)
ax1.set_title("Second Dose Administered,")
ax1.set_xlabel("number of people")
ax1.set_ylabel("Second Dose Administered,")
fig.tight_layout()
fig.savefig("Second Dose Administered")
