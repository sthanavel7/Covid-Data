import pandas as pd
import plotly.express as px
df=pd.read_csv("Covid.csv")
fig=px.scatter(df,x="date",y="cases")
fig.show() 