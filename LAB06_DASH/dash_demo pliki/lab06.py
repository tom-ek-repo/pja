from dash import Dash, dcc, html,Input, Output,State, dash_table
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dash.exceptions import PreventUpdate

app = Dash(__name__)

url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
w = pd.read_csv(url2, sep=";")
w['color']= 'white'
r = pd.read_csv(url1, sep=";")
r['color']='red'
w=pd.concat([w,r])
w.to_pickle('./w.pkl', compression='zip') 

# w=pd.read_pickle('w.pkl',compression='zip')

all_options1={
    'wykres1' : ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density','sulphates','alcohol','quality','color'],
    'wykres2' : ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']
}

colors = {
    'background': '#F5F7E3',
    'text':  '#111111'
}

app.layout = html.Div(
    style={'backgroundColor': colors['background']}, 
    children=[
    html.H1(
        children='Lab 6 -  Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Tabela danych winequality (red+white)'  , style={ 'textAlign': 'left',  'color': colors['text'] }),
    dash_table.DataTable(w.head(10).to_dict('records'), [{"name": i, "id": i} for i in w.columns]),
    html.Div([ html.Br(), html.Br()]),
    html.Div(children='Analiza danych  (red + white)'  , style={ 'textAlign': 'left',  'color': colors['text'] }),
    html.Div([dcc.Dropdown( ['wykres1', 'wykres2'],placeholder= 'Wybierz wykres',id='dropdown')]), 
    # html.Div([dcc.Dropdown( [] ,
    #          placeholder='Wybierz zmienną',id='dropdown1')]), 
    

    html.Div([    dcc.RadioItems(
                id='dropdown1'
                ,labelStyle={'display': 'inline-block', 'marginTop': '15px'}
            )]),

    html.Div([ dcc.Graph(id='plot-1')])  
])

@app.callback(
    Output('plot-1', 'figure'),
    Input('dropdown', 'value'),
    Input('dropdown1', 'value'),
    State('dropdown', 'value'),
    State('dropdown1', 'value')
    )
def update_graph( selection ,selection1,start, start1):
    fig= px.scatter() #pusty sykres
    
    if 'wykres1' == selection  and selection1!=''  and start and start1:   
        x,y,z = (w['pH'],w[selection1] ,w['color'])
        fig  = px.scatter(x, y ,color=z )
        fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'] ) 
        fig.update_xaxes(title=x.name,   type='linear' )
        fig.update_yaxes(title=y.name,type='linear')

    if 'wykres2' == selection  and selection1!='' and start and start1:   
        x,y,z = (w['color'], w[selection1] ,w['color'])
        fig  = px.scatter(x, y ,color=z )
        fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'] ) 
        fig.update_xaxes(title=x.name,   type='linear' )
        fig.update_yaxes(title=y.name,type='linear')
    return fig

@app.callback(
    Output('dropdown1', 'options'),
    Input('dropdown', 'value'))
def set_options(selected):
    #   if not selected:
        #  raise PreventUpdate
    return [{'label':i,'value':i} for i in all_options1[selected]]
    # return [i for i in all_options1[selected]]

@app.callback(
    Output('dropdown1', 'value'),
    Input('dropdown1', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(dev_tools_hot_reload=True,debug=True)

