from django.urls import path

from .import views

urlpatterns = [
    path('', views.lista_topicos, name ='topicos'),
    path('new', views.new_topico, name='new_topico'),
    path('<int:pk>/', views.post, name='post'),
 	path('newpost', views.new_post, name = 'new_post'),
 	path('newcoment', views.new_coment, name = 'new_coment'),
 	path('contato/', views.contato, name='contato'),
    path('contato/obg', views.obg, name='obg'),

 	   
 		   

]