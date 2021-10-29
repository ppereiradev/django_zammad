import plotly.io as pio
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash

pio.templates.default = "ggplot2"

app = DjangoDash('zammad_dashboard', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.UNITED])
#server = app.server