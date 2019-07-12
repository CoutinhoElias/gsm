
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect

from material import *
# Create your views here.
from gsm.persons.forms import ClientsForm, AddressForm, EmployeeForm
from gsm.persons.models import Person, Address, Client

# class NewCadastroPessoaView(LayoutMixin,):
#     title = "Nova Pessoa 87"
#
#     model = Person# model Person
#
#     layout = Layout(
#         # Campos do Persons
#         Fieldset("Inclua uma pessoa",
#                  Row('name', ),
#                  Row('birthday','purchase_limit'),
#                  Row('address1', ),
#                  ),
#         #Inline dos endereços
#         Inline('Endereços 98', AddressInline,),
#
#     )
#
#     def forms_valid(self, form, inlines):
#         self.object = form.save(commit=False)
#         #self.object.person_id = self.request.user.id
#         self.object.save()
#         return super(NewCadastroPessoaView, self).forms_valid(form, inlines)
#
#     def get_success_url(self):
#         return self.object.get_absolute_url()


# class NewCadastroPessoaView1(LayoutMixin,):
#     title = "Nova Pessoa 87"
#
#     model = Person# model Person
#
#     layout = Layout(
#         # Campos do Persons
#         Fieldset("Inclua uma pessoa",
#                  Row('name', ),
#                  Row('birthday','purchase_limit'),
#                  Row('address1', ),
#                  ),
#         #Inline dos endereços
#         Inline('Endereços SEMFORM', AddressInline,),
#
#     )
#
#     #print('Chegou na linha 340')
#
#     def forms_valid(self, form, inlines):
#         self.object = form.save(commit=False)
#         #self.object.person_id = self.request.user.id
#         self.object.save()
#         return super(NewCadastroPessoaView, self).forms_valid(form, inlines)
#
#     def get_success_url(self):
#         return self.object.get_absolute_url()

# --------------------------------------------------------------------------------------------------


# def clients_list(request):
#     context = {
#         'clients_list': Client.objects.all()
#     }
#     return render(request, 'persons/person_list.html', context)

def clients_list(request):
    q = request.GET.get('search_box')
    print(request.GET)
    if q:
        print(q)
        clients = Client.objects.filter(name__icontains=q)
    else:
        clients = Client.objects.all()
    context = {'clients': clients}
    print(context)
    return render(request, 'persons/person_list.html', context)


def clients(request):
    if request.method == 'POST':

        form = ClientsForm(request.POST)
        #address = AddressForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()
            return redirect(new)
            #return HttpResponseRedirect('/reserva/listagem/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            print(form)
            return render(request, 'person.html', {'form':form})
    else:
        context = {'form': ClientsForm()}
        return render(request, 'person.html', context)


def clients_edit(request, person_id):
    pessoa = get_object_or_404(Client, pk=person_id)
    if request.method == 'POST':
        form = ClientsForm(request.POST, instance=pessoa)
        addressform = AddressForm(request.POST, instance=pessoa)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()
            return HttpResponseRedirect('/cadastro/clientes/editar/'+person_id, person_id)
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            print(form)
            return render(request, 'person.html', {'form':form})
    else:
        print('Entrou em modo de edição do cliente '+person_id)

        request.session['person_id'] = person_id
        print('A variável person_id da session já possui o valor: '+request.session['person_id'])

        person_instance = Person.objects.get(pk=request.session["person_id"])
        initial_data = {"person": person_instance}

        context = {'form': ClientsForm(instance=pessoa), 'addressform': AddressForm(initial=initial_data)}
        return render(request, 'persons/person_addresses.html', context)


def employees(request):
    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()

            return HttpResponseRedirect('/reserva/listagem/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            return render(request, 'person.html', {'form':form})
    else:
        context = {'form': EmployeeForm()}
        return render(request, 'person.html', context)


def address(request):
    if 'person_id' in request.session:

        if request.method == 'POST':
            #request.session['elias'] = 'cabeção'
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'+ request.session['person_id'])

            form = AddressForm(request.POST)

            if form.is_valid():
                print('<<<<==== FORM VALIDO ====>>>>')
                new = form.save()

                return HttpResponseRedirect('/cadastro/clientes/editar/'+request.session["person_id"])
            else:
                print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
                print(form)
                return render(request, 'persons/person_address.html', {'form':form})
        else:
            person_instance = Person.objects.get(pk=request.session["person_id"])
            initial_data = {"person": person_instance}
            context = {'form': AddressForm(initial=initial_data)}

            return render(request, 'persons/person_address.html', context)
    else:
        return HttpResponseRedirect('/cadastro/clientes/listar/') #fuincionando mais ou menos, verificar o motivo de estar caindoaqui
