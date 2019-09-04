from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.person_create, name='person_create'),
    path('<int:id>/editar/', views.person_update, name='person_update'),
    path('listar/', views.person_client_list, name='person_client_list'),
]