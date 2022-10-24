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



# html.H1 is the <h1> </h1> html object
FILL_IN = html.H1("Hello, Best Talent Group Ever!")

colors = {"background": "white", "text": "black"}

# TODO 1:
# fig = px.bar()

app.layout = html.Div(
    children=[
        html.H1(FILL_IN, style={"textAlign": "center", "color": colors["text"]},),
        html.Div(
            children="Dit is het dashboard van: ________",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        # TODO 2:

    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
