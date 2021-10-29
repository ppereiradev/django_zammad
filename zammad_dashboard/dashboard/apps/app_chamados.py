import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from ..app import app


def layout_chamados(clean_data):

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




    fig_bar_stacked = px.bar(
        clean_data['df-created'],
        x=clean_data['df-created'].index,
        y="qnt",
        color="state",
        barmode="stack",
        labels={'state':'Estado', 'qnt': 'Quantidade', 'created_at':''},
        category_orders={'Estado':['Novo', 'Aberto','Pendente','Aguardando Resposta','Retorno','Resolvido','Fechado']},
        color_discrete_sequence=['red', 'orange', 'yellow', 'blue', 'darkblue', 'purple', 'green'],
    )

    fig_bar_stacked.update_xaxes(tickformat='%d-%m-%Y')

    fig_bar_stacked.update_layout(legend_title_text='Estado:',legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
    ))






    ######### FIRST ROW #########
    ''' SUMMARY CARDS' CONTENT '''
    content_hoje_row0 = [
        dbc.CardHeader("Tempo Médio Fechar Chamado", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [
                html.P(str(int(clean_data['tempo-medio-fechar-chamado-hora'])) + " horas",className="card-text cards-content-info-body-chamados"),
            ]
        ),
    ]

    content_mensal_row0 = [
        dbc.CardHeader("Tempo Médio Para Primeira Resposta", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [
                html.P(str(int(clean_data['tempo-medio-primeiro-contato-minuto'])) + " minutos",className="card-text cards-content-info-body-chamados"),
            ]
        ),
    ]

    content_media_row0 = [
        dbc.CardHeader("Média de Chamados Abertos por Dia", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [
                html.P(str(int(clean_data['media-aberto-chamado-dia'])) + " chamados",className="card-text cards-content-info-body-chamados"),
            ]
        ),
    ]

    content_cota_row0 = [
        dbc.CardHeader("Média de Chamados Fechados por Dia", className='cards-content-info-header-chamados'),
        dbc.CardBody(
            [   
                html.P(str(int(clean_data['media-fechar-chamado-dia'])) + " chamados",className="card-text cards-content-info-body-chamados"),
            ],
        ),
    ]


    row0 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_hoje_row0, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_mensal_row0, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_media_row0, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_cota_row0, className='shadow cards-info-chamados'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )

    ''' END RESUMO CARDS' CONTENT '''
    ##############################

    ######### SECOND ROW #########

    content_bar_stacked1 = [
        dbc.CardHeader("Quantidade de Chamados por Estado", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=fig_bar_stacked,
                animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
            ]
        ),
    ]

    row1 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_bar_stacked1, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-12 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )
    ##############################

    ######### THIRD ROW #########

    content_pie_row2 = [
        dbc.CardHeader("5 Cursos que os Discentes mais Abrem Chamados", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=go.Figure(data=[go.Pie(labels=clean_data['df-joined']['curso'].value_counts().index[:5], values=clean_data['df-joined']['curso'].value_counts()[:5])]).update_layout(showlegend=False),
                animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
            ]
        ),
    ]


    content_bar_row2 = [
        dbc.CardHeader("5 Setores que os Técnicos mais Abrem Chamados", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=go.Figure(data=[go.Pie(labels=clean_data['df-joined']['lotacao'].value_counts().index[:5], values=clean_data['df-joined']['lotacao'].value_counts()[:5])]).update_layout(showlegend=False),
                animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
            ]
        ),
    ]

    row2 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_pie_row2, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_bar_row2, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )

    ''' END CHART CARDS' CONTENT '''
    ##############################


    ######### FOURTH ROW #########
    ''' CHART CARDS' CONTENT '''
    content_consumo_row3 = [
        dbc.CardHeader("Abertura de Chamados Mensal", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(id='slider-graph-chamados',animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
                dcc.Slider(id='slider-udpdatemode-chamados',
                    marks={i: f'{i}' for i in range(20)},
                    max=21,
                    value=20,
                    step=1,
                    updatemode='drag'),
            ]
        ),
    ]

    content_media_row3 = [
        dbc.CardHeader("Abertura de chamados por setor", className='cards-content-chart-header-chamados'),
        dbc.CardBody(
            [
                dcc.Graph(figure=fig_map, animate=True),
            ]
        ),
    ]


    row3 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(content_consumo_row3, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(content_media_row3, className='card border-light shadow cards-chart-chamados'), className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
                className="mb-4",
            ),
        ]
    )
    ''' END CHART CARDS' CONTENT '''
    ##############################

    ''' final layout render '''
    layout = html.Div([html.Div([row0, row1, row2, row3])])



    import math
    @app.callback(Output('slider-graph-chamados', 'figure'),
                [Input('slider-udpdatemode-chamados', 'value')])
    def display_value_chamado(value):
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