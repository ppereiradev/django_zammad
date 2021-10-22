from django.urls import path
from . import views
from .dashboard import dashboard

urlpatterns = [
    path('energia-e-agua/', views.dashboard, name='eixo_7_energia'),
]
