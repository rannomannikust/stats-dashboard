from dash import html, dcc
from translation import translations


def sidebar_layout(lang="et"):
    return html.Div([
    html.H2(translations[lang]["sidebar.title"], style={"padding": "10px"}),
    html.Hr(),
            # Põhimenüü: Salary
        html.Div([
            dcc.Link(translations[lang]["sidebar.salary"], href="/economy",
                     style={"display": "block", "padding": "10px", "font-weight": "bold"}),

            # Alammenüü lingid
            html.Div([
                dcc.Link(translations[lang]["sidebar.salary.longterm"], href="/economy/longterm",
                         style={"display": "block", "padding": "5px 20px"}),
                dcc.Link(translations[lang]["sidebar.salary.shortterm"], href="/economy/shortterm",
                         style={"display": "block", "padding": "5px 20px"}),
            ])
        ]),
    #dcc.Link(translations[lang]["sidebar.salary"], href="/economy", style={"display": "block", "padding": "10px"}),
    dcc.Link(translations[lang]["sidebar.env"], href="/enviroment", style={"display": "block", "padding": "10px"}),
    dcc.Link(translations[lang]["sidebar.pop"], href="/population", style={"display": "block", "padding": "10px"}),
], style={
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12%",
    "backgroundColor": "#f8f9fa",
    "padding": "20px",
    "overflow": "auto"
})


