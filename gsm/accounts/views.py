from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = '/accounts/login/'


register = RegisterView.as_view()


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#
#         if form.is_valid():
#             print('<<<<==== FORM VALIDO ====>>>>')
#             new = form.save(commit=False)
#             new.save()
#             #form.save_m2m()
#
#             return redirect(settings.LOGIN_URL)
#         else:
#             print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
#             return render(request, 'register.html', {'form': form})
#     else:
#         context = {'form': RegistrationForm()}
#         return render(request, 'register.html', context)


# def user_detail(request):
#     user_detalhe = User.objects.filter(user=request.user)
#     context = {'user_detail': user_detalhe}
#     return render(context)
