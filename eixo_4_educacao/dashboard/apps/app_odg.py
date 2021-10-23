import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

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


cursos = ["Administração", "Administração UAST", "Agronomia", "Agronomia UAST", "Bacharelado em Agroecologia", "Bacharelado em Ciência da Computação", "Bacharelado em Ciências Biológicas", "Bacharelado em Ciências Biológicas - UAST", "Bacharelado em Ciências do Consumo", "Bacharelado em Ciências Econômicas", "Bacharelado em Ciências Econômicas - UAST", "Bacharelado em Ciências Sociais", "Bacharelado em Gastronomia", "Bacharelado em Sistemas da Informação", "Bacharelado em Sistemas da Informação - UAST", "Economia Doméstica", "Engenharia Agrícola e Ambiental", "Engenharia Ambiental", "Engenharia Civil - UACSA", "Engenharia da Computação - Belo Jardim", "Engenharia de Controle e Automação - Belo Jardim", "Engenharia de Materiais- UACSA", "Engenharia de Pesca", "Engenharia de Pesca - UAST", "Engenharia Elétrica - UACSA", "Engenharia Eletrônica - UACSA", "Engenharia Florestal", "Engenharia Hídrica - Belo Jardim", "Engenharia Mecânica - UACSA", "Engenharia Química - Belo Jardim", "Licenciatura em Ciências Agrícolas", "Licenciatura em Ciências Biológicas", "Licenciatura em Computação", "Licenciatura em Educação Física", "Licenciatura em Física", "Licenciatura em História", "Licenciatura em Letras (Português e Espanhol)", "Licenciatura em Matemática", "Licenciatura em Pedagogia", "Licenciatura em Química", "Licenciatura em Química - UAST", "Medicina Veterinária", "Zootecnia", "Zootecnia - UAST"]

import random
#Generate 44 random numbers between 10 and 100
randomlist = random.sample(range(10, 100), 44)

fig_evasao_curso = go.Figure()
fig_evasao_curso.add_trace(go.Bar(x=cursos, y=randomlist,
                marker_color='crimson',))

fig_evasao_curso.update_layout(
    xaxis_title="Curso",
    yaxis_title="Porcentagem",
)


x0 = np.random.randn(500) + 23
# Add 1 to shift the mean of the Gaussian distribution
x1 = np.random.randn(500) + 25

fig_evasao_sexo = go.Figure()
fig_evasao_sexo.add_trace(go.Histogram(x=x0, name='Masculino'))
fig_evasao_sexo.add_trace(go.Histogram(x=x1, name='Feminino'))

# Overlay both histograms
fig_evasao_sexo.update_layout(barmode='overlay',
    xaxis_title="Idade",
    yaxis_title="Porcentagem",
    legend_title="Sexo",
)
# Reduce opacity to see both histograms
fig_evasao_sexo.update_traces(opacity=0.75)


x0 = np.random.randn(500) + 20
# Add 1 to shift the mean of the Gaussian distribution
x1 = np.random.randn(500) + 18

fig_matricula_sexo = go.Figure()
fig_matricula_sexo.add_trace(go.Histogram(x=x0, name='Masculino'))
fig_matricula_sexo.add_trace(go.Histogram(x=x1, name='Feminino'))

# Overlay both histograms
fig_matricula_sexo.update_layout(barmode='overlay',
    xaxis_title="Idade",
    yaxis_title="Porcentagem",
    legend_title="Sexo",
)
# Reduce opacity to see both histograms
fig_matricula_sexo.update_traces(opacity=0.75)



######### FIRST ROW #########
''' SUMMARY CARDS' CONTENT '''

content_mensal_matricula_row0 = [
    dbc.CardHeader("Média de Matrícula Último Semestre", className='cards-content-info-header-odg'),
    dbc.CardBody(
        [
            html.P("2800",className="card-text cards-content-info-body-odg"),
        ]
    ),
]

content_media_matricula_row0 = [
    dbc.CardHeader("Media Renovação de Matrícula", className='cards-content-info-header-odg'),
    dbc.CardBody(
        [
            html.P("1600",className="card-text cards-content-info-body-odg"),
        ]
    ),
]


content_evasao_anual_row0 = [
    dbc.CardHeader("Média de Evasão Anual", className='cards-content-info-header-odg'),
    dbc.CardBody(
        [
            html.P("43%",className="card-text cards-content-info-body-odg"),
        ]
    ),
]


content_ultimo_semestre_row0 = [
    dbc.CardHeader("Média de Evasão Último Semestre", className='cards-content-info-header-odg'),
    dbc.CardBody(
        [
            html.P("30%",className="card-text cards-content-info-body-odg"),
        ]
    ),
]

row0 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(content_mensal_matricula_row0, className='shadow cards-info-odg'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                dbc.Col(dbc.Card(content_media_matricula_row0, className='shadow cards-info-odg'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                dbc.Col(dbc.Card(content_evasao_anual_row0, className='shadow cards-info-odg'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
                dbc.Col(dbc.Card(content_ultimo_semestre_row0, className='shadow cards-info-odg'), className='mb-4 col-lg-3 col-md-12 col-sm-12 col-xs-12 col-12'),
            ],
            className="mb-4",
        ),
    ]
)

''' END RESUMO CARDS' CONTENT '''
##############################

######### SECOND ROW #########
''' CHART CARDS' CONTENT '''
content_evasao_curso_row1 = [
    dbc.CardHeader("Média de Evasão Semestral por Curso", className='cards-content-chart-header-odg'),
    dbc.CardBody(
        [
            dcc.Graph(figure=fig_evasao_curso,
            animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
        ]
    ),
]



''' CHART CARDS' CONTENT '''
content_evasao_sexo_row1 = [
    dbc.CardHeader("Média de Evasão Semestral de Alunos por Sexo", className='cards-content-chart-header-odg'),
    dbc.CardBody(
        [
            dcc.Graph(figure=fig_evasao_sexo, id='slider-graph-odg',animate=True, style={'backgroundColor':'#1a2d46', 'color':'#fffff'}),
        ]
    ),
]


content_matricula_sexo_row1 = [
    dbc.CardHeader("Média de Matrícula Semestral de Alunos por Sexo", className='cards-content-chart-header-odg'),
    dbc.CardBody(
        [
            dcc.Graph(figure=fig_matricula_sexo,
            animate=True),
        ]
    ),
]



row1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(content_evasao_curso_row1, className='card border-light shadow cards-chart-odg'),  className='mb-4 col-xl-12 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                dbc.Col(dbc.Card(content_evasao_sexo_row1, className='card border-light shadow cards-chart-odg'),  className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                dbc.Col(dbc.Card(content_matricula_sexo_row1, className='card border-light shadow cards-chart-odg'),  className='mb-4 col-xl-6 col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
            ],
            className="mb-4",
        ),
    ]
)

''' END CHART CARDS' CONTENT '''
##############################


''' final layout render '''
layout = html.Div([
    html.Div([row0, row1])
],)



import math
@app.callback(Output('slider-graph-odg', 'figure'),
            [Input('slider-udpdatemode-odg', 'value')])

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
    [Output("progress-odg", "value"), Output("progress-odg", "children")],
    [Input("progress-interval-odg", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""

