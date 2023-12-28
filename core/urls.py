from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('paciente/', views.paciente, name="paciente"),
    path('prueba/', views.prueba, name="prueba"),
]