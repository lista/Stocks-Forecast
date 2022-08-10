import dash
from dash import dcc 
from dash import html 
import dash_daq as daq
from datetime import datetime as dt 

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.H1('Stock Predictor Dashboard', className='start-head'),
        html.P("Welcome to the Stock Predictor Dashboard App!", className="start"),
        html.Img(),
        html.Div([
          # stock code input
        ]),
        html.Div([
          # Date range picker input
        ]),
        html.Div([
           # Stock price button
           # Indicators button
           # Number of days of forecast input
           # Forecast button
        ])
    ], style={'padding': 10, 'flex': 3}),
    html.Div([
        html.Div([
            # logo
            # company name
        ]),
        html.Div(
            # description 
            id="description", className="decription_ticker"),
        html.Div([
            #  stock price plot
        ], id="graphs-content"),
        html.Div([
            # indicator plot
        ], id="main-content"),
        html.Div([
            # forecast plot
        ], id="forecast-content")
    ],className="content", style={'flex': 9} )
], style={'display': 'flex', 'flex-direction': 'row'})
if __name__ == '__main__':
    app.run_server(debug=True)