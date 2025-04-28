from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos_list, name='eventos'),
    path('sponsors/', views.sponsors_list, name='sponsors'),
    
]
