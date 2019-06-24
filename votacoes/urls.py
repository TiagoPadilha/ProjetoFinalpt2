from django.urls import path

from . import views

urlpatterns = [
    
    path('jogos/', views.lista_jogos, name ='jogos'),
    path('jogos/<int:pk>/', views.jogo, name='jogo'),
    path('jogos/novo_jogo', views.new_votacao, name='new_jogo'),
    path('jogos/novo_time', views.new_time, name='new_time'),
]