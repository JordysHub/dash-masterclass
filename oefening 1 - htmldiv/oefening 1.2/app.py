'''
Oefening 1.2:
Maak naast de header een subtitel onder de header (maak hiervan gebruik van children en de html.H1 en html.Div componenten).
Gebruik de styling argument om de styling van de tekst te veranderen. Gebruik hiervoor de dict 'layout_dict'.
https://dash.plotly.com/layout
'''

from dash import Dash, html, dcc

layout_dict = {
    'backgroundColor': 'lightgreen',
    'header': 'darkblue',
    'text': 'darkred',
    'textAlign': 'center',
    }

FILL_IN_1: # TODO (styling div component)
FILL_IN_2: # TODO (header)
FILL_IN_3: # TODO (subtitle)


app = Dash(__name__)

app.layout = html.Div(style = FILL_IN_1, children=[

    # TODO FILL_IN_2
    # TODO FILL_IN_3


])


if __name__ == "__main__":
    app.run_server(debug=True)