"""
Oefening 3.1:
Make yourself comfortable, want hier blijven we voorlopig wel even!
Zoals gezegd zijn de callbacks hetgeen het dashboard echt tot leven gaat brengen. Hiervoor gaan we eerst een dropdown menu maken als input voor onze filter.
De belangrijskte properties van het menu zijn: 'id' (deze hebben we nodig voor de callback), 'value' en 'options'.


# TODO 1
Maak een dropdownmenu :).
Gebruik eventueel de documentatie van https://dash.plotly.com/dash-core-components/dropdown
"""


import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

df = pd.read_csv("./data/night_out.csv")
fig = px.bar(df, x="City", y="Cost", color="Category")

# TODO 1: DROPDOWN MENU

DROP_DOWN_MENU = dcc.Dropdown()


app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            html.H1("Hello, Best Talent Group Ever!"), style={"textAlign": "center", "color": "darkblue"}
        ),
        html.H2(
            children="Let's Party!",
            style={"textAlign": 'center', "color": 'red', 'font-weight': 'bold'},
        ),

        # TODO
        DROP_DOWN_MENU,

        dcc.Graph(id="my-graph", figure=fig),

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
