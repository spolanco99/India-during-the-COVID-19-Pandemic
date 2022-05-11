#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:13:15 2022

@author: samanthapolanco
"""

import pandas as pd 
import os 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt

vaccine_status = pd.read_csv("covid_vaccine_statewise.csv")

vaccine_status.info()


fig,ax1=plt.subplots()
sns.set(rc={'figure.figsize':(12,8)})
sns.barplot(data="Females(Individuals Vaccinated)", ax=ax1)
ax1.set_title("Females(Individuals Vaccinated)")
ax1.set_xlabel("vaccine status")
ax1.set_ylabel("Female(Individuals Vaccinated)")
fig.tight_layout()
fig.savefig("Female(Individuals Vaccinated).png")


