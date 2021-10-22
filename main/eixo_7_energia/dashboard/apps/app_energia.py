import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from ..app import app

######### FIGURES CHARTS #########
fig_cota = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 8000,
    mode = "gauge+number+delta",
    delta = {'reference': 3800},
    gauge = {'axis': {'range': [None, 10000]},
             'bar': {'color': "#FEBD11"},
             'steps' : [
                 {'range': [0, 5000], 'color': "lightgray"},
                 {'range': [5000, 7000], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 9900}}))





d = {'Predio':['Reitoria','STD','CEGEN','DELOGS'], 'Consumo': [3000, 4000, 5000, 6000], 'lat':['-8.014212','-8.018282','-8.017475','-8.015940'], 'lon':['-34.950411','-34.949333','-34.950096','-34.946378']}
df = pd.DataFrame(data=d)
df["lat"] = pd.to_numeric(df["lat"], downcast="float")
df["lon"] = pd.to_numeric(df["lon"], downcast="float")

df_diffq = (df["Consumo"].max() - df["Consumo"].min()) / 49
df["scale"] = (df["Consumo"] - df["Consumo"].min()) / df_diffq + 30



fig_map = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="Predio", hover_data=["Consumo"],
                        color="Consumo", color_continuous_scale=px.colors.sequential.Oranges,
                        size=df["scale"], size_max=50, zoom=15, height=500)
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



years = ['2016','2017','2018']

fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(x=years, y=[500, 600, 700],
                base=[-500,-600,-700],
                marker_color='crimson',
                name='expenses'))
fig_bar.add_trace(go.Bar(x=years, y=[300, 400, 700],
                base=0,
                marker_color='lightslategrey',
                name='revenue'
                ))





######### FIRST ROW #########
''' SUMMARY CARDS' CONTENT '''
content_demanda_row0 = [
    dbc.CardHeader("Demanda - kW", className='cards-content-info-header-energia'),
    dbc.CardBody(
        [
            html.P("1800",className="card-text cards-content-info-body-energia"),
        ]
    ),
]


content_hoje_row0 = [
    dbc.CardHeader("Consumo Hoje - kWh", className='cards-content-info-header-energia'),
    dbc.CardBody(
        [
            html.P("3800",className="card-text cards-content-info-body-energia"),
        ]
    ),
]

content_mensal_row0 = [
    dbc.CardHeader("Consumo Mensal - kWh", className='cards-content-info-header-energia'),
    dbc.CardBody(
        [
            html.P("2800",className="card-text cards-content-info-body-energia"),
        ]
    ),
]

content_media_row0 = [
    dbc.CardHeader("Media - kWh", className='cards-content-info-header-energia'),
    dbc.CardBody(
        [
            html.P("2800",className="card-text cards-content-info-body-energia"),
        ]
    ),
]

content_cota_row0 = [
    dbc.CardHeader("Cota Mensal Atingida", className='cards-content-info-header-energia'),
    dbc.CardBody(
        [   #dcc.Interval(id="progress-interval-energia", n_intervals=0, interval=500),
            #dbc.Progress(id="progress-energia", style={"height":"50%", "margin-top":"5%", 'color':'#FEBD11'}),
            html.P("28%",className="card-text cards-content-info-body-energia"),
        ],
    ),
]


row0 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(content_demanda_row0, className='shadow cards-info-energia')),
                dbc.Col(dbc.Card(content_hoje_row0, className='shadow cards-info-energia')),
                dbc.Col(dbc.Card(content_mensal_row0, className='shadow cards-info-energia')),
                dbc.Col(dbc.Card(content_media_row0, className='shadow cards-info-energia')),
                dbc.Col(dbc.Card(content_cota_row0, className='shadow cards-info-energia')),
            ],
            className="mb-4",
        ),
    ]
)

''' END RESUMO CARDS' CONTENT '''
##############################

######### SECOND ROW #########
''' CHART CARDS' CONTENT '''
content_speed_row1 = [
    dbc.CardHeader("Consumo - kWh", className='cards-content-chart-header-energia'),
    dbc.CardBody(
        [
            dcc.Graph(figure=fig_cota,animate=True),
        ]
    ),
]


content_pie_row1 = [
    dbc.CardHeader("Consumo Médio - kWh", className='cards-content-chart-header-energia'),
    dbc.CardBody(
        [
            dcc.Graph(figure=go.Figure(data=[go.Pie(labels=['Reitoria','STD','CEGEN','DELOGS'], values=[4500, 2500, 1053, 500])]),
            animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
        ]
    ),
]


content_bar_row1 = [
    dbc.CardHeader("Consumo Médio - kWh", className='cards-content-chart-header-energia'),
    dbc.CardBody(
        [
            dcc.Graph(figure=fig_bar,
            animate=True),
        ]
    ),
]

row1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(content_speed_row1, className='card border-light shadow cards-chart-energia'), className='col-4'),
                dbc.Col(dbc.Card(content_pie_row1, className='card border-light shadow cards-chart-energia'), className='col-4'),
                dbc.Col(dbc.Card(content_bar_row1, className='card border-light shadow cards-chart-energia'), className='col-4'),
            ],
            className="mb-4",
        ),
    ]
)

''' END CHART CARDS' CONTENT '''
##############################


######### THIRD ROW #########
''' CHART CARDS' CONTENT '''
content_consumo_row2 = [
    dbc.CardHeader("Consumo - kWh", className='cards-content-chart-header-energia'),
    dbc.CardBody(
        [
            dcc.Graph(id='slider-graph-energia',animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
            dcc.Slider(id='slider-udpdatemode-energia',
                marks={i: f'{i}' for i in range(20)},
                max=21,
                value=20,
                step=1,
                updatemode='drag'),
        ]
    ),
]

content_media_row2 = [
    dbc.CardHeader("Consumo - kWh", className='cards-content-chart-header-energia'),
    dbc.CardBody(
        [
            dcc.Graph(figure=fig_map, animate=True),
        ]
    ),
]


content_media2_row2 = [
    dbc.CardHeader("Consumo Médio - kWh", className='cards-content-chart-header-energia'),
    dbc.CardBody(
        [
            dcc.Graph(figure=px.scatter(px.data.tips(), x="total_bill", y="tip", trendline="ols"),
            animate=True),
        ]
    ),
]


row2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(content_consumo_row2, className='card border-light shadow cards-chart-energia'), className='col-4'),
                dbc.Col(dbc.Card(content_media_row2, className='card border-light shadow cards-chart-energia'), className='col-4'),
                dbc.Col(dbc.Card(content_media2_row2, className='card border-light shadow cards-chart-energia'), className='col-4'),
            ],
            className="mb-4",
        ),
    ]
)
''' END CHART CARDS' CONTENT '''
##############################

''' final layout render '''
layout = html.Div([
    html.Div([row0, row1, row2])
],)



import math
@app.callback(Output('slider-graph-energia', 'figure'),
            [Input('slider-udpdatemode-energia', 'value')])

def display_value(value):
    x = []
    y = []
    for i in range(value):
        x.append(i)
        y.append(math.sqrt(i))

    graph = go.Scatter(
        x=x,
        y=y,
        name='ROOT SQUARE'
    )

    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis = {'range':[min(x), max(x)]},
        yaxis = {'range':[min(y), max(y)]},
        font={'color':'white'},
    )

    return {'data': [graph],'layout': layout}




@app.callback(
    [Output("progress-energia", "value"), Output("progress-energia", "children")],
    [Input("progress-interval-energia", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""

