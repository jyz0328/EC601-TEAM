import pandas as pd
import numpy as np 
import plotly.express as px
import seaborn as sns
import plotly.offline as py
import plotly.graph_objects as go


nutrients=pd.read_csv("csvfile.csv")
nutrients.head()

nutrients=nutrients.replace("t",0)
nutrients=nutrients.replace("t'",0)

nutrients.head()

nutrients=nutrients.replace(",","", regex=True)
nutrients['Fiber']=nutrients['Fiber'].replace("a","", regex=True)
nutrients['Calories'][91]=(8+44)/2

nutrients.dtypes

print(nutrients.isnull().any())
print('-'*245)
print(nutrients.describe())
print('-'*245)

nutrients=nutrients.dropna()
nutrients.shape