import dash
from bot import search_amazon
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options



app.layout = html.Div(children=[
    html.H1(children='Amazon Bot'),

    dcc.Input(
        id="my_product",
        type="search",
        value="",
        placeholder="Please enter your product"),

    html.Button(
        "Submit",
        id="submit",
        n_clicks=0),

    html.Div(id="result")

])
alerts = html.Div(
    [
        dbc.Alert("This is an alert!", color="primary")
    ])

@app.callback(
    Output("result", "children"),
    Input("submit", "n_clicks"),
    Input("my_product", "value"))


def update_result(submit, my_product):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "submit" in changed_id:
        search_amazon(my_product)
        return "Your Product has been added"




if __name__ == '__main__':
    app.run_server(debug=True)