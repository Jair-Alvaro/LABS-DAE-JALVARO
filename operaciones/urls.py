from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sumar/<int:numero_1>/<int:numero_2>',views.suma,name='suma'),
    path('restar/<int:numero_1>/<int:numero_2>',views.resta,name='resta'),
    path('multiplicar/<int:numero_1>/<int:numero_2>',views.multiplicacion,name='multiplicacion'),    

]