from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from gsm.person.forms import PersonForm, ContactFormSet, FileDocumentFormSet


def person_create1(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            # form.save_m2m()

            return HttpResponseRedirect('/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            print(form)
            return render(request, 'person_create_contact.html', {'form': form})
    else:
        context = {'form': PersonForm()}
        return render(request, 'person_create_contact.html', context)


def person_create2(request):
    # Cria variável na session
    request.session['person_id'] = 1

    if request.method == 'POST':
        form = PersonForm(request.POST)

        # Retira toda validação do campo
        form.errors.pop('user')

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return HttpResponseRedirect('/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            return render(request, 'person_create_contact.html', {'form': form})
    else:
        context = {'form': PersonForm()}

        # Exclui variável da session
        del request.session['person_id']

        return render(request, 'person_create_contact.html', context)


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        contact_formset = ContactFormSet(request.POST)
        file_document_formset = FileDocumentFormSet(request.POST)

        if form.is_valid() and contact_formset.is_valid() and file_document_formset.is_valid():
            with transaction.atomic():

                person_form = form.save()
                contact_formset.instance = person_form
                contact_formset.save()

                file_document_formset.instance = person_form
                file_document_formset.save()

                return redirect('/')

    else:
        form = PersonForm()

        contact_formset = ContactFormSet()

        file_document_formset = FileDocumentFormSet()

    forms = [file_document_formset.empty_form] + file_document_formset.forms + \
            [contact_formset.empty_form] + contact_formset.forms
    context = {'form': form,
               'contact_formset': contact_formset,
               'file_document_formset': file_document_formset,
               'forms': forms}
    return render(request, 'person_create_contact.html', context)
