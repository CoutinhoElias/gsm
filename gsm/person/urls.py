from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.person_create, name='person_create'),
    path('novaa/', views.create_person, name='create_person'),
    # path('nova/', views.CreatePerson.as_view(), name='CreatePerson'),
    path('<int:id>/editar/', views.person_update, name='person_update'),
    path('listar/', views.person_client_list, name='person_client_list'),
]