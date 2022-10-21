from dash import Dash, html, dcc

app = Dash(__name__)

# html.H1 is the <h1> </h1> html object
FILL_IN = html.Div(html.H1("Hello, Best Talent Group Ever!"), style={'color': 'blue'})

app.layout = html.Div([FILL_IN])




if __name__ == "__main__":
    app.run_server(debug=True)

