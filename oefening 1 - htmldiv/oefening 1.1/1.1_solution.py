'''
Oefening 1.1:
Gebruikt een Dash Html Component om in de app layout "Hello, Best Talent Group Ever!" te plaatsen.
'''

from dash import Dash, html


# TODO
FILL_IN = html.H1("Hello, Best Talent Group Ever!")


app = Dash(__name__)

app.layout = FILL_IN



if __name__ == "__main__":
    app.run_server(debug=True)
