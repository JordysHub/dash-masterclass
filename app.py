from dash import Dash, html, dcc

# px creates entire figure at once
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Dataframe which will be used for the dashboard
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

# declare figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# reusable component: Insert


# here the layout of a page is determined, using html.Divs. dash.html has a component class for each HTML tag.
app.layout = html.Div([
                        # This generates: <h1>Hello Dash</h1>
                        html.H1(children=[
                            "Hello, Dash!"], style={'textAlign': 'center'}),
                        html.Br(),
                        # dash.dcc contains components like Graph, dropdows and more which renders interactive visualisations
                        dcc.Graph(
                            id='example-graph',
                            figure=fig
                        )
                    ])


if __name__ == '__main__':
    app.run_server(debug=True)