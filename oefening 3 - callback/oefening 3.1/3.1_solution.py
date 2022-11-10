import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate


df = pd.read_csv("./data/night_out.csv")
fig = px.bar(df, x="City", y="Cost", color="Category")

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            html.H1("Hello, Best Talent Group Ever!"),
            style={"textAlign": "center", "color": "darkblue"},
        ),
        html.H2(
            children="Let's Party!",
            style={"textAlign": 'center', "color": 'red', 'font-weight': 'bold'},
        ),
        dcc.Dropdown(
            id="my-dropdown",
            options=[{"label": x, "value": x} for x in sorted(df.Category.unique())],
            placeholder="Please select a Category...",
            clearable=True,
            style={
                "border-color": "#12A19B",
                "border-width": "3px",
                "border-radius": "10px",
                "width": "60%",
                "font-size": "14px",
                "color": "red",
                "padding-left": "85px",
            },
            persistence=True, # keeps value of dropdown menu when reloading
            multi=False,      # select multiple values
        ),
        dcc.Graph(id="my-graph", figure=fig)
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
