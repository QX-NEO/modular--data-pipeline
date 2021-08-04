import functions
import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


modular_data = pd.read_sql_query('select * from modular', functions.get_sql()) 
app = dash.Dash(__name__)



app.layout = html.Div([
    html.H1("Modular Coding Test", style={'text-align': 'center'}),
    html.Div([
        html.H2(children='Indicative Value of Aggregated Holding of FPIS', style={'text-align': 'left'}),
        html.Div(children='Input ISIN:'),
        html.Div(dcc.Input(id='input-on-submit', type='text')),
        html.Button('Submit', id='submit-val',n_clicks=0),
        html.Div(id='container-button-basic',
             children='Enter a value and press submit'),
    html.Br(),
    dcc.Graph(id='visuals', figure={})  
    ])

])


@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    Output(component_id='visuals', component_property='figure'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])

def update_output(n_clicks, value):
    string_val = str(value).upper()
    unique = modular_data[modular_data["ISIN"] == string_val]
    fig = px.line(unique, x="date", y="IVAH", title='Indicative Value of Aggregated Holding of FPIS vs Date')
    return 'The input value was: {}'.format(string_val),fig



if __name__ == '__main__':
    app.run_server(debug=True)