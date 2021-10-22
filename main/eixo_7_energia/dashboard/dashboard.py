import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from .app import app
from .apps import app_energia, app_agua



app.layout = html.Div([
    dbc.Tabs(
    [
        dbc.Tab(app_energia.layout, label="Energia", tab_style={"marginLeft": "auto"}),
        dbc.Tab(app_agua.layout, label="Água"),
    ],
    className='mb-3',id='tabs-app'),

    html.Div(id='tabs-content')
])


""" app.layout = html.Div([
    dcc.Tabs(id="tabs-app", value='tab-1-energia', children=[
        dcc.Tab(label='Energia', value='tab-1-energia'),
        dcc.Tab(label='Água', value='tab-2-agua'),
    ],className='mb-3'),

    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs-app', 'value'))
def render_content(tab):
    if tab == 'tab-1-energia':
        return app_energia.layout

    elif tab == 'tab-2-agua':
        return app_agua.layout

 """
