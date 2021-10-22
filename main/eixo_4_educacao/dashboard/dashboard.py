import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from .app import app
from .apps import app_odg, app_docentes



app.layout = html.Div([
    dbc.Tabs(
    [
        dbc.Tab(app_odg.layout, label="ODG", tab_style={"marginLeft": "auto"}),
        dbc.Tab(app_docentes.layout, label="Docentes"),
    ],
    className='mb-3',id='tabs-app'),

    html.Div(id='tabs-content')
])
