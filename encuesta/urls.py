from django.urls import path
from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    #path('', views.index),
    path('' , views.hola),
    path('detalle', views.detalle),
    path('results/<int:pregunta_id>', views.resultados),
    path('vote/<int:pregunta_id>', views.votar),
    
]
