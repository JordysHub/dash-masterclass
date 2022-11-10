import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

'''Read dataframe'''
df = pd.read_csv("./data/night_out.csv")


'''Styling dict'''
layout_dict = {
    'backgroundColor': 'lightgreen',
    'header': 'darkblue',
    'text': 'darkred',
    'textAlign': 'center'
    }



# TODO 1: DROPDOWN

DROPDOWN_CONTENT = dcc.Dropdown()


# TODO 2: GRAPHS

GRAPH_CONTENT = dcc.Graph()


# TODO 3: CALLBACKS

INPUT_CONTENT = Input()
OUTPUT_CONTENT = Output()


# TODO 4: UPDATE_FUNCTION



app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            html.H1("Hello, Best Talent Group Ever!"), style={"textAlign": "center", "color": "darkblue"}
        ),

        html.P(
            children="Welcome to this Masterclass",
            style={"textAlign": layout_dict["textAlign"], "color": layout_dict["text"]},
        ),


        # TODO 1
        DROPDOWN_CONTENT,

        # TODO 2
        GRAPH_CONTENT
    ]
)


@app.callback(
    # TODO 3
    OUTPUT_CONTENT,
    INPUT_CONTENT
)

def update_output_fig(input_value):

    # TODO 4

    new_df = # fill in
    fig = px.bar(new_df, x="City", y="Cost", color="Category")

    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
