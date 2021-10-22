from django.urls import path
from . import views
from .dashboard import dashboard

urlpatterns = [
    path('educacao/', views.dashboard, name='eixo_4_energia'),
]
