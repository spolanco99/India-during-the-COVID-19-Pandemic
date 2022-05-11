
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:13:15 2022

@author: samanthapolanco
"""

import pandas as pd 
import os 
import seaborn as sns 
import matplotlib.pyplot as plt

vaccine_status = pd.read_csv("covid_vaccine_statewise.csv")


fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=vaccine_status["Female(Individuals Vaccinated)"], ax=ax1)
ax1.set_title("Female(Individuals Vaccinated)")
ax1.set_xlabel("vaccine status")
ax1.set_ylabel("Female(Individuals Vaccinated)")
fig.tight_layout()
fig.savefig("Female(Individuals Vaccinated).png")


fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.lineplot(data=vaccine_status["Male(Individuals Vaccinated)"], ax=ax1)
ax1.set_title("Male(Individuals Vaccinated)")
ax1.set_xlabel("vaccine status")
ax1.set_ylabel("Male(Individuals Vaccinated)")
fig.tight_layout()
fig.savefig("Male(Individuals Vaccinated).png")