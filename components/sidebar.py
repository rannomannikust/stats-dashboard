from dash import html, dcc

sidebar = html.Div([
    html.H2("Valikud", style={"padding": "10px"}),
    html.Hr(),
    dcc.Link("Gross monthly salary", href="/economy", style={"display": "block", "padding": "10px"}),
    dcc.Link("Enviroment", href="/enviroment", style={"display": "block", "padding": "10px"}),
    dcc.Link("Population", href="/population", style={"display": "block", "padding": "10px"}),
], style={
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "15%",
    "backgroundColor": "#f8f9fa",
    "padding": "20px",
    "overflow": "auto"
})
