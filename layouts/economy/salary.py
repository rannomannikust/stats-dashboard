from dash import html, dcc
import plotly.express as px
import pandas as pd
from utils.stat_api import get_pa103_data

df = get_pa103_data(indicator="GR_W_AVG", emtak="TOTAL")

fig = px.line(df, x="aasta", y="väärtus",
              title="Keskmine brutokuupalk kõigil aastatel",
              labels={"väärtus": "Brutokuupalk €"})

salary_layout = html.Div([
    html.H3("Brutokuupalk – PA103"),
    dcc.Graph(figure=fig)
])
