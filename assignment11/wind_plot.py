import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type='pandas')

print("FIRST 10 ROWS:\n", df.head(10))
print("LAST 10 ROWS:\n", df.tail(10))

df['strength'] = df['strength'].str.replace('[^\d.]', '', regex=True)
df['strength'] = df['strength'].astype(float)

fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs. Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'}
)

fig.write_html("wind.html", auto_open=True)