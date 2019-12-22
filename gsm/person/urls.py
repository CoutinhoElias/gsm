from django.urls import path

from . import views

app_name = 'person'

urlpatterns = [
    path('novo/', views.person_create, name='person_create'),
    # path('nova/', views.PersonFormView, name='PersonFormView'),
    path('nova/', views.PersonFormView.as_view(), name='PersonFormView'),
    # path('nova/', views.CreatePerson.as_view(), name='CreatePerson'),
    path('<int:id>/editar/', views.person_update, name='person_update'),
    path('listar/', views.person_client_list, name='person_client_list'),
]
