#Import All the required libraries
import datetime
import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web

#Create user interface using Dash Libraries
app = dash.Dash()
app.title = "Stock Visualisation"

app.layout = html.Div(children=[
    html.H1("Stock Market Dashboard"),
    html.H4("Please enter the Stock Name"),
    dcc.Input(id='input', value='APPL', type='text'),
    html.Div(id= 'output-graph')
])

#Code for Reading & Creating Dashboard
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_graph(input_data):
    start = datetime.datetime(2010, 1 , 1)
    end = datetime.datetime.now()

    try:
        df = web.DataReader(input_data, 'google', start, end)

        graph = dcc.Graph(id="example", figure={
            'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data}],
            'layout' :{
                'title':input_data
            }
        })

    except:
        graph = html.Div("Error retrieving stock data.")

    return graph


if __name__ == '__main__':
    app.run_server()


