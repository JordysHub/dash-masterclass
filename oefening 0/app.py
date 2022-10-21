# import of all dash component libraries
from dash import Dash, html, dcc

# declaration of the Dash app
app = Dash(__name__)

# declaration of the layout of the app. 
app.layout = html.Div()

# run the app server on the localhost.
if __name__ == "__main__":
    app.run_server(debug=True)
