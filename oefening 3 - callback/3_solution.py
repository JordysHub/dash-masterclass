import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate


df = pd.read_csv("./data/night_out.csv")

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
            placeholder="Please select a Category...",
            clearable=True,
            style={
                "border-color": "#12A19B",
                "border-width": "3px",
                "border-radius": "10px",
                "width": "60%",
                "font-size": "14px",
                "color": "red",
                "padding-left": "85px",
            },
            persistence=True, # keeps value of dropdown menu when reloading
            multi=False,      # select multiple values
        ),
        html.Br(),
        dcc.Dropdown(id="my-dummy-input", disabled=True, style = {"padding-left": "85px", "width": "60%"}),
        dcc.Graph(id="my-graph", figure={}),
    ]
)

@app.callback(
    Output(component_id="my-graph", component_property="figure"),
    [Input(component_id="my-dropdown", component_property="value"),
     Input(component_id="my-dummy-input", component_property="value")]
)
def update_output_fig(dropdown, dummy):
    if dropdown is None:
        # raise PreventUpdate
        fig = px.bar(df, x="City", y="Cost", color="Category")

    if dropdown is not None:
        dff = df[df["Category"] == dropdown]
        fig = px.bar(dff, x="City", y="Cost", color="Category")

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
