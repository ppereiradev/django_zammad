from django.urls import path
from . import views
from .dashboard import dashboard

urlpatterns = [
    path('', views.dashboard, name='zammad_dashboard'),
]
