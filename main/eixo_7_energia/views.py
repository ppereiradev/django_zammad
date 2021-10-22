from django.shortcuts import render

# Create your views here.
def dashboard(requests):
    return render(requests,'eixo_7_energia/dashboard.html')