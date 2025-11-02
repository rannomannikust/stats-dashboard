import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from components.sidebar import sidebar
from layouts.economy.salary import salary_layout
from layouts.environment.envirStatus import envirstatus_layout
from layouts.population.ive import ive_layout

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Stats Dashboard"
app.layout = html.Div([
    dcc.Location(id="url"),
    dcc.Store(id="language-store", data="et"),  # ← globaalne keel
    html.Div([
        html.Label("Vali keel:", style=
                   {
                    "marginRight": "10px",
                    "alignSelf": "center"
                    }),
        dcc.Dropdown(
            id="language-dropdown",
            options=[
                {"label": "Eesti", "value": "et"},
                {"label": "English", "value": "en"}
            ],
            value="et",
            clearable=False,
            style={"width": "200px"}
        )
    ], style={"display": "flex", "justifyContent": "flex-end", "padding": "10px"}),
    #    "display": "flex","justifyContent": "flex-end","padding": "10px"
    #     "padding": "10px", "marginLeft": "20%"
    sidebar,
    html.Div(id="page-content", style={"marginLeft": "20%", "padding": "20px"})
])


@app.callback(
        Output("page-content", "children"),
        Input("url", "pathname"))

def display_page(pathname):
    if pathname == "/enviroment":
        return envirstatus_layout
    elif pathname == "/population":
        return ive_layout
    else:
        return salary_layout  # default

if __name__ == "__main__":
    app.run(debug=True)