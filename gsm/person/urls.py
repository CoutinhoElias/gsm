from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.person_create, name='person_create'),
    path('<int:pk>/editar/', views.person_update, name='person_update'),
]