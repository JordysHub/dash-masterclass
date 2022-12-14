'''
Oefening 1.2:
Maak naast de header een subtitel onder de header (maak hiervan gebruik van de html.H1 en html.H3 of html.P componenten).
Omdat dit meerdere componenten zijn, zetten we deze in een list. Deze list zetten we in de 'children' property van een html.Div (hierover later meer).

Gebruik de styling property om de styling van de tekst te veranderen. Gebruik hiervoor de dict 'layout_dict'.
https://dash.plotly.com/layout
'''

from dash import Dash, html

layout_dict = {
    'backgroundColor': 'lightgreen',
    'header': 'darkblue',
    'text': 'darkred',
    'textAlign': 'center',
    }


# TODO 1: Voeg hier de styling van het Div component toe
# FILL_IN_1 =

# TODO 2: Voeg hier de header toe + styling
# FILL_IN_2 =

# TODO 3: Voeg hier een subtitle toe + styling
# FILL_IN_3 =


app = Dash(__name__)

app.layout = html.Div(style = FILL_IN_1, children=[

    FILL_IN_2,
    FILL_IN_3


])


if __name__ == "__main__":
    app.run_server(debug=True)