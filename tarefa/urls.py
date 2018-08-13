from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_tarefa, name='lista_tarefa'),
    path('tarefa/<int:pk>/', views.tarefa_detail, name='tarefa_detail'),
    path('tarefa/new', views.tarefa_new, name='tarefa_new'),
    path('tarefa/<int:pk>/edit/', views.tarefa_edit, name='tarefa_edit'),
]
