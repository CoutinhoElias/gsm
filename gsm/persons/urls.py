from django.conf.urls import url, include
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path('funcionarios/', views.employees, name='employees'),
    # url(r'clientes/editar/(?P<person_id>\d+)/endereco/$', address, name='address'),
    path('clientes/endereco/novo/', views.address, name='address'),
    path('clientes/listar/', views.clients_list, name='clients_list'),
    path('clientes/', views.clients, name='clients'),
    path('clientes/editar/<int:pk>/', views.clients_edit, name='clients_edit'),

    # path('clientes/notas/lista/', views.InvoiceSingleTableView.as_view(), name='invoice_list'),
    path('clientes/notas/nova/', views.InvoiceFormView.as_view(), name='invoice_add'),
    path('clientes/notas/edita/<int:id>/', views.InvoiceUpdateView.as_view(), name='invoice_edit'),

    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
