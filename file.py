import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("sports.csv")
print(df)
print(df.groupby("level")["attempt"].mean())
figure=go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["level 1","level 2","level 3","level 4"],
    orientation="h"
))
figure.show()