from django.conf.urls import url, include
from django.urls import path
from django.views.i18n import JavaScriptCatalog


# from danibraz.persons.views import employees, clients, clients_edit, address, clients_list
from . import views
from gsm.persons.views import clients, clients_list, employees, address, clients_edit

urlpatterns = [
    # url(r'cliente/$', NewProfissoesPessoaView.as_view(), name='clients'),
    # url(r'^pessoa/', views.NewCadastroPessoaView1.as_view(template_name="persons/person_and_professions.html")),
    # url(r'^pessoas/', views.NewCadastroPessoaView.as_view(template_name="persons/form.html")),

    path('funcionarios/', views.employees, name='employees'),

    # url(r'clientes/editar/(?P<person_id>\d+)/endereco/$', address, name='address'),
    path('clientes/endereco/novo/', views.address, name='address'),

    path('clientes/listar/', views.clients_list, name='clients_list'),

    path('clientes/', views.clients, name='clients'),

    path('clientes/editar/<int:pk>/', views.clients_edit, name='clients_edit'),



    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
