from dash import Dash, dcc, html, Input, Output
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


df = pd.read_csv("night_out.csv")

layout_dict = {
    "backgroundColor": "lightgreen",
    "header": "darkblue",
    "text": "darkred",
    "textAlign": "center",
}

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            html.H1("Hello, Best Talent Group Ever!"),
            style={"textAlign": "center", "color": "darkblue"},
        ),
        html.P(
            children="Welcome to this Masterclass",
            style={"textAlign": layout_dict["textAlign"], "color": layout_dict["text"]},
        ),
        dcc.Dropdown(
            id="my-dropdown",
            options=[{"label": x, "value": x} for x in sorted(df.Category.unique())],
            value="",
        ),
        dcc.Graph(id="bar_chart", figure={}),
        # TODO 1: zorg dat de juiste output id in de html.P komt
        html.H4("Totaal uitgegeven:"),
        html.P(),
    ]
)

@app.callback(
    Output(component_id="bar_chart", component_property="figure"),
    Input(component_id="my-dropdown", component_property="value"),
)
def update_output_fig(input_value):
    df = pd.read_csv("night_out.csv")
    dff = df[df["Category"] == input_value]
    fig = px.bar(dff, x="City", y="Cost", color="Category")
    return fig


# TODO 2 vul de juiste input id in
input_id = "to fill"


@app.callback(Output("text_output", "children"), Input(input_id, "clickData"))
def capture_hover_data(clickData):
    # TODO 3: bereken het totaal uitgaven van de geselecteerde stad
    sum_of_city = 0
    return sum_of_city


if __name__ == "__main__":
    app.run_server(debug=True)
