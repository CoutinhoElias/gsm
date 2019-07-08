from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from gsm.accounts import views

app_name = 'accounts'


urlpatterns = [

    path('', include('django.contrib.auth.urls')),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', LoginView.as_view, {'template_name': 'registration/login.html'}, name='login'),
    path('alterar-senha/',
         views.PasswordChangeView.as_view(template_name='password_change_form.html'),
         name='password_change'),

    path('senha-alterada/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('registro/', views.register, name='register'),




    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
