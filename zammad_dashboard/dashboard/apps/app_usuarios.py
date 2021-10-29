import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from ..app import app


def layout_usuarios(clean_data):

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





    d = {'Predio':['Reitoria','STD','CEGEN','DELOGS'], 'Chamados': [3000, 4000, 5000, 6000], 'lat':['-8.014212','-8.018282','-8.017475','-8.015940'], 'lon':['-34.950411','-34.949333','-34.950096','-34.946378']}
    df = pd.DataFrame(data=d)
    df["lat"] = pd.to_numeric(df["lat"], downcast="float")
    df["lon"] = pd.to_numeric(df["lon"], downcast="float")

    df_diffq = (df["Chamados"].max() - df["Chamados"].min()) / 49
    df["scale"] = (df["Chamados"] - df["Chamados"].min()) / df_diffq + 30



    fig_map = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="Predio", hover_data=["Chamados"],
                            color="Chamados", color_continuous_scale=px.colors.sequential.Oranges,
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
    content_hoje_row0_user = [
        dbc.CardHeader("USUARIOS TESTE", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [
                html.P(str(int(clean_data['tempo-medio-fechar-chamado-hora'])) + " horas",className="card-text cards-content-info-body-chamados"),
            ]
        ),
    ]

    content_mensal_row0_user = [
        dbc.CardHeader("USUARIOS TESTE", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [
                html.P(str(int(clean_data['tempo-medio-primeiro-contato-minuto'])) + " minutos",className="card-text cards-content-info-body-chamados"),
            ]
        ),
    ]

    content_media_row0_user = [
        dbc.CardHeader("USUARIOS TESTE", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [
                html.P(str(int(clean_data['media-aberto-chamado-dia'])) + " chamados",className="card-text cards-content-info-body-chamados"),
            ]
        ),
    ]

    content_cota_row0_user = [
        dbc.CardHeader("USUARIOS TESTE", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [   
                html.P(str(int(clean_data['media-fechar-chamado-dia'])) + " chamados",className="card-text cards-content-info-body-chamados"),
            ],
        ),
    ]


    row0_user = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_hoje_row0_user, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_mensal_row0_user, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_media_row0_user, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_cota_row0_user, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )

    ''' END RESUMO CARDS' CONTENT '''
    ##############################

    ######### SECOND ROW #########
    ''' CHART CARDS' CONTENT '''
    content_speed_row1_user = [
        dbc.CardHeader("Chamados Abertos", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=fig_cota,animate=True),
            ]
        ),
    ]


    content_pie_row1_user = [
        dbc.CardHeader("5 Cursos que os Discentes mais Abrem Chamados", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=go.Figure(data=[go.Pie(labels=clean_data['df-joined']['curso'].value_counts().index[:5], values=clean_data['df-joined']['curso'].value_counts()[:5])]).update_layout(showlegend=False),
                animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
            ]
        ),
    ]


    content_bar_row1_user = [
        dbc.CardHeader("5 Setores que os Técnicos mais Abrem Chamados", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=go.Figure(data=[go.Pie(labels=clean_data['df-joined']['lotacao'].value_counts().index[:5], values=clean_data['df-joined']['lotacao'].value_counts()[:5])]).update_layout(showlegend=False),
                animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
            ]
        ),
    ]

    row1_user = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_speed_row1_user, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-4 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_pie_row1_user, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-4 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_bar_row1_user, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-4 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )

    ''' END CHART CARDS' CONTENT '''
    ##############################


    ######### THIRD ROW #########
    ''' CHART CARDS' CONTENT '''
    content_consumo_row2_user = [
        dbc.CardHeader("Abertura de Chamados Mensal", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(id='slider-graph-usuarios',animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
                dcc.Slider(id='slider-udpdatemode-usuarios',
                    marks={i: f'{i}' for i in range(20)},
                    max=21,
                    value=20,
                    step=1,
                    updatemode='drag'),
            ]
        ),
    ]

    content_media_row2_user = [
        dbc.CardHeader("Abertura de chamados por setor", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=fig_map, animate=True),
            ]
        ),
    ]

    """ 
    content_media2_row2_user = [
        dbc.CardHeader("Consumo Médio - kWh", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=px.scatter(px.data.tips(), x="total_bill", y="tip", trendline="ols"),
                animate=True),
            ]
        ),
    ]
    """

    row2_user = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_consumo_row2_user, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_media_row2_user, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )
    ''' END CHART CARDS' CONTENT '''
    ##############################

    ''' final layout render '''
    layout = html.Div([html.Div([row0_user, row1_user, row2_user]),],)



    import math
    @app.callback(Output('slider-graph-usuarios', 'figure'),
                [Input('slider-udpdatemode-usuarios', 'value')])

    def display_value_usuario(value):
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


    return layout