from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from gsm.person.forms import PersonForm, ContactFormSet, FileDocumentFormSet
from gsm.person.models import Person


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        contact_formset = ContactFormSet(request.POST, request.FILES)
        file_document_formset = FileDocumentFormSet(request.POST, request.FILES)

        if form.is_valid() and contact_formset.is_valid() and file_document_formset.is_valid():
            with transaction.atomic():

                person_form = form.save()

                contact_formset.instance = person_form
                contact_formset.save()

                file_document_formset.instance = person_form
                file_document_formset.save()

                return redirect('/pessoa/listar/')
        else:
            print(file_document_formset)
            return render(request, 'person_create_contact.html',
                          {'form': form,
                           'contact_formset': contact_formset,
                           'file_document_formset': file_document_formset})
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


def person_update(request, id):
    # Pega a chave da URL acima com (request, pk)
    # joga na variável invoice na linha abaixo passando o modelo MESTRE e os parâmetros que desejo como filtro
    person = get_object_or_404(Person, id=id)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        contact_formset = ContactFormSet(request.POST, request.FILES, instance=person)
        file_document_formset = FileDocumentFormSet(request.POST, request.FILES, instance=person)

        if form.is_valid() and contact_formset.is_valid() and file_document_formset.is_valid():
            with transaction.atomic():

                person_form = form.save()

                contact_formset.instance = person_form
                contact_formset.save()

                file_document_formset.instance = person_form
                file_document_formset.save()

                return redirect('/pessoa/listar/')
            # return redirect('/pergunta/' + str(question.pk) + '/editar')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')

            print('/n-------------------------', file_document_formset)
            return render(request, 'person_create_contact.html',
                          {'form': form,
                           'contact_formset': contact_formset,
                           'file_document_formset': file_document_formset})
    else:
        form = PersonForm(instance=person)

        contact_formset = ContactFormSet(instance=person)

        file_document_formset = FileDocumentFormSet(instance=person)

    forms = [file_document_formset.empty_form] + file_document_formset.forms + \
            [contact_formset.empty_form] + contact_formset.forms
    context = {'form': form,
               'contact_formset': contact_formset,
               'file_document_formset': file_document_formset,
               'forms': forms}
    return render(request, 'person_create_contact.html', context)


@login_required
def person_client_list(request):
    q = request.GET.get('searchInput')
    # print(request.GET)
    if q:
        persons = Person.objects.filter(Q(name__icontains=q))

    else:
        # persons = Person.objects.none()
        persons = Person.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(persons, 13)

    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)

    context = {'persons': persons}
    return render(request, 'person_client_list.html', context)