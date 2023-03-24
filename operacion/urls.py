from django.urls import path
from . import views
#OPERACIONES
urlpatterns = [
    # ex: localhost:8080/polls/
    #path('', views .index),
    path('suma/<int:valor1>/<int:valor2>' , views.sumar),

]
