from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_Inicial, name='index'),
    path('jogos/', views.lista_jogos, name ='jogos'),
    path('jogos/<int:pk>/', views.jogo, name='jogo'),
]