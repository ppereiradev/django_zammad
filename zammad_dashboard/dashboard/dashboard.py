import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from .app import app
from .apps import app_chamados, app_usuarios

# It Returns a dictionary with all data needed to build the charts:
#
# dict = {
#  'tempo-medio-fechar-chamado-hora': tempo_medio_fechar_chamado_hora,
#  'tempo-medio-primeiro-contato-minuto': tempo_medio_primeiro_contato_minuto, 
#  'df-created': df_created,
#  'df-joined': df_joined,
# }
#
from .data.get_data import cleaning_data

clean_data = cleaning_data()

app.layout = html.Div([
    dbc.Tabs([
            dbc.Tab(app_chamados.layout_chamados(clean_data), label="Chamados", tab_style={"marginLeft": "auto"}),
            dbc.Tab(app_usuarios.layout_usuarios(clean_data), label="Usuários"),
        ], className='mb-3',id='tabs-app'),
    dcc.Interval(id='interval-component',interval=10*1000, n_intervals=0)
])

@app.callback(Output('tabs-app', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):

    clean_data = cleaning_data()

    return [
            dbc.Tab(app_chamados.layout_chamados(clean_data), label="Chamados", tab_style={"marginLeft": "auto"}),
            dbc.Tab(app_usuarios.layout_usuarios(clean_data), label="Usuários"),
        ]