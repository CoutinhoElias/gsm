from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.financeiro_create, name='financeiro_create'),
    path('<int:id>/editar/', views.financeiro_update, name='financeiro_update'),
    path('listar/', views.financeirot_list, name='financeirot_list'),
    path('<int:pk>/list/', views.financeirot_client_list, name='financeirot_client_list'),
]
