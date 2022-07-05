# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:27:20 2022

@author: Satya
"""

import pandas as pd
import numpy as np
import os
import scipy as sp
import seaborn as sns
import dash 
import dash_html_components as html
import dash_core_components as dcc




os.chdir("E:/Google Drive/Github/Dashboards/Dashboarding/Titanic")
test =pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

# Data Wrangling on Test Dataset

# Check how many missing value naN
train.isna().sum()

train.describe()
train['Age'].describe()
sns.displot(train, x="Age")

"""
1. There are 891 Passengers.
2. Cabin has 687 missing values. The variable needs to be dropped.
3. Age has 177 missing values. There are some options for Age 
Replacing with average will not make sense as distribution is skewed left. 

"""
# App Instantiation
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello, World!')
])

if __name__ =='__main__':
    app.run_server()
    


