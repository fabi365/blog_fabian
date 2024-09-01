from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('post/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('post/new/', views.agregar_publicacion, name='agregar_publicacion'),
    path('post/<int:pk>/edit/', views.editar_publicacion, name='editar_publicacion'),
]
