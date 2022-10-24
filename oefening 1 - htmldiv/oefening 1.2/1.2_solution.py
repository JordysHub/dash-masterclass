'''
Oefening 1.2:
Maak naast de header een subtitel onder de header (maak hiervan gebruik van children en de html.H1 en html.P componenten).
Gebruik de styling parameter om de styling van de tekst te veranderen. Gebruik hiervoor de dict 'colors'.
https://dash.plotly.com/layout
'''


from dash import Dash, html, dcc


layout_dict = {
    'backgroundColor': 'lightgreen',
    'header': 'darkblue',
    'text': 'darkred',
    'textAlign': 'center'
    }


app = Dash(__name__)


app.layout = html.Div(style = {'backgroundColor': 'lightgreen'}, children=[

    html.H1(children="Hello, Best Talent Group Ever!" , style = {'textAlign': layout_dict['textAlign'], 'color': layout_dict['header']}),
    html.P(children= "Welcome to this Masterclass", style = {'textAlign': layout_dict['textAlign'], 'color': layout_dict['text']}),

])


if __name__ == "__main__":
    app.run_server(debug=True)