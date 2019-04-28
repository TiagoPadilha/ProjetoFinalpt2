from django.urls import path

from .import views

urlpatterns = [
    path('forum/', views.lista_topicos, name ='topicos'),
    path('forum/new', views.new_topico, name='new_topico'),
    path('forum/<int:pk>/', views.post, name='post'),
 	path('forum/newpost', views.new_post, name = 'new_post'),
 	path('forum/newcoment', views.new_coment, name = 'new_coment'),

 	   
 		   

]