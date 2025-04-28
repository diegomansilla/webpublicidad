from django.urls import path
from . import views
from eventos.views import crear_superusuario

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos_list, name='eventos'),
    path('sponsors/', views.sponsors_list, name='sponsors'),
    
]
