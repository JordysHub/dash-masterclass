'''
Oefening 1.2:
Maak naast de header een subtitel onder de header (maak hiervan gebruik van children en de html.H1 en html.Div componenten).
Gebruik de styling parameter om de styling van de tekst te veranderen. Gebruik hiervoor de dict 'colors'.
https://dash.plotly.com/layout
'''


from dash import Dash, html, dcc

app = Dash(__name__)

colors = {
    'background': 'lightblue',
    'header': 'black',
    '': ''
    }


FILL_IN_1: {'background': '', 'textAlign': ''}
FILL_IN_2: {'textAlign': '', 'color': ''}
FILL_IN_3: {'textAlign': '', 'color': ''}

# FILL_IN_1: {'background': colors[background]}
# FILL_IN_2: {'textAlign': 'center', 'color': colors[header]}
# FILL_IN_3: {'textAlign': 'center', 'color': colors[text]}




app.layout = html.Div(style = FILL_IN_1, children=[

    # TODO 1.2


    # html.H1(children="Hello, Best Talent Group Ever!" , style = FILL_IN_2),
    # html.Div(children= "Welcome to this Masterclass", style = FILL_IN_3)



])



if __name__ == "__main__":
    app.run_server(debug=True)