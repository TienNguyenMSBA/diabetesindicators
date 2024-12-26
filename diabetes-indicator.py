
# Install the ucimlrepo package
# pip install pandas certifi
# pip install ucimlrep


# Import the dataset into your code
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
cdc_diabetes_health_indicators = fetch_ucirepo(id=891) 
  
# data (as pandas dataframes) 
X = cdc_diabetes_health_indicators.data.features 
y = cdc_diabetes_health_indicators.data.targets 
  
# metadata 
print(cdc_diabetes_health_indicators.metadata) 
  
# variable information 
print(cdc_diabetes_health_indicators.variables) 

# Exploratory Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt





