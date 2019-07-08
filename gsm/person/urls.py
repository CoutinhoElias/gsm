from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.person_create, name='person_create'),
]