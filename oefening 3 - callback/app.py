"""
Oefening 3:
Make yourself comfortable, want hier blijven we voorlopig wel even!
Zoals gezegd zijn de callbacks hetgeen het dashboard echt tot leven gaat brengen.
De callback maakt gebruik van een Input en Ouput. Deze hebben beide 2 argumenten: het component_id en de component_property.
Vervolgens maken we een callback functie welke deze argumenten gebruikt als input en output. Over het algemeen wil je in deze functie je data filteren
en een nieuw dataframe retourneren.

Enkele tips:
- Je kunt in je functie ook printstatements maken om te debuggen of voor extra feedback.
- Ga niet het originele dataframe wijzigen, maar maak een kopie.


# TODO 1:
Maak de Input() en Ouput() voor ons dashboard.
Gebruik hiervoor eventueel de documentatie van https://dash.plotly.com/basic-callbacks.

# TODO 2:
Maak hier de update functie welke de Input en Output gebruikt om ons dashboard te filteren.

# TODO Bonus Opgave 3:
- Maak de callbacks zo dat beide categorieen ("date night" en "party night") allebei worden geladen als het dashboard wordt geopend.
- Maak de callbacks zo dat geen enkele categorie (i.e. een lege grafiek) wordt weergegeven als het dashboard wordt geopend.
"""

import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

df = pd.read_csv("./data/night_out.csv")


# TODO 1: CALLBACKS

INPUT_CONTENT = Input()
OUTPUT_CONTENT = Output()


# TODO 2: UPDATE_FUNCTION

'''Zie onderaan deze file'''


app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            html.H1("Hello, Best Talent Group Ever!"), style={"textAlign": "center", "color": "darkblue"}
        ),
        html.H3(
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
                "height": "45px",
                "width": "60%",
                "font-size": "18px",
                "color": "#cbc1c1",
                "padding-left": "85px",
            },
            persistence=True,
            multi=False,
        ),
        dcc.Graph(id="my-graph", figure={}),

    ]
)

@app.callback(
    # TODO 1
    OUTPUT_CONTENT,
    INPUT_CONTENT
)

def update_output_fig(input_value):

    # TODO 2

    return



if __name__ == "__main__":
    app.run_server(debug=True)