import dash                     # pip install dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px     # pip install plotly==5.2.2

import pandas as pd             # pip install pandas


df = pd.read_csv(
    r'https://raw.githubusercontent.com/EpitechMscProPromo2023/T-MAJ-800-DAT_15/master/donnee.csv?token=GHSAT0AAAAAABVVQCW6NRAOBBQT2OUAXH7SYWUKGLA')
df["Date"] = pd.to_datetime(df["Date"])
time = df["Date"]
hum = df["Humidite"]
print(df.head())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Analytics Dashboard",
            style={"textAlign": "center"}),
    html.Hr(),
    html.P("Choose your town:"),
    html.Div(html.Div([
        dcc.Dropdown(id='animal-type', clearable=False,
                     value="TROMELIN",
                     options=[{'label': x, 'value': x} for x in
                              df["Nom"].unique()]),
    ], className="two columns"), className="row"),

    html.Div(id="output-div", children=[]),
])


@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="animal-type", component_property="value"),
              )
def make_graphs(animal_chosen):
    # HISTOGRAM
    df_hist = df[df["Nom"] == animal_chosen]
    fig_hist = px.histogram(df_hist, x="Temperature")
    fig_hist.update_xaxes(categoryorder="total descending")

    # humidité

    fig_strip = px.histogram(df_hist, x="Date", y="Humidite")

   
    fig_line = px.scatter(
        df_hist, x=df_hist["Date"], y=df_hist["Precipitation"])

    return [
        html.Div([
            html.H2("Température (Kelvin)", style={"textAlign": "center"}),
            html.Div([dcc.Graph(figure=fig_hist)], className="twelve columns"),
        ], className="row"),
        html.Hr(),
        html.H2("Précipitation", style={"textAlign": "center"}),
        html.Div([
            html.Div([dcc.Graph(figure=fig_line)],
                     className="twelve columns"),
        ], className="row"),
        html.Hr(),
        html.H2("Humidité", style={"textAlign": "center"}),
        html.Div([
            html.Div([dcc.Graph(figure=fig_strip)],
                     className="twelve columns"),
        ], className="row"),
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
