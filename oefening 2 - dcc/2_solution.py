"""
Oefening 2:
Hier gaan we aan de slag met dash core components (dcc).
Deze worden gebruikt om objecten neer te zetten zoals controls en graphs.

TODO 1:
Maak een px.bar figure bij TODO 1. Documentatie hiervan is eventueel te vinden in de plotly documentatie.
https://plotly.com/python/bar-charts/

TODO 2:
Gebruik een dcc component om een graph in de html.Div() van de app.layout te maken.
https://dash.plotly.com/dash-core-components/graph
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {"background": "white", "text": "black"}
df = pd.read_csv("./data/night_out.csv")

# TODO 1:
fig = px.bar(df, x="City", y="Cost", color="Category")

app.layout = html.Div(
    children=[
        html.H1(html.H1("Hello, Best Talent Group Ever!"), style={"textAlign": "center", "color": colors["text"]},),
        html.Div(
            children="Dit is het dashboard van: ________",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        # TODO 2
        dcc.Graph(
            id="cost_per_country",
            figure = fig
        )

    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
