from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db import transaction
from django.db.models import Q
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import FormView
from material.base import LayoutMixin, Layout, Fieldset, Row, Span9, Span4, Span12, Span3, Span2, Span8, Span5

from gsm.core.materialLayout import Inline
from gsm.person.forms import PersonForm, FileDocumentFormSet, ContactForm
from gsm.person.models import Person, FilesDocuments, Contact


# def create_person(request):
#     template_name = 'person_create0.html'
#     person_form = Person()
#     person_document_formset = inlineformset_factory(
#         Person,
#         FilesDocuments,
#         form=FilesDocumentsForms,
#         extra=0,
#         min_num=1,
#         validate_min=True,
#     )
#     if request.method == 'POST':
#         form = PersonForm(request.POST, request.FILES, instance=person_form,prefix='main')
#         formset = person_document_formset(request.POST, request.FILES, instance=person_form, prefix='person')
#         if form.is_valid() and formset.is_valid():
#             form = form.save()
#             formset.save()
#             url = 'person:create_person'
#             return HttpResponseRedirect(resolve_url(url, form.pk))
#     else:
#         form = PersonForm(instance=person_form, prefix='main')
#         formset = person_document_formset(instance=person_form, prefix='person')
#     context = {'form': form, 'formset': formset}
#     return render(request, template_name, context)


# class FilesDocumentsInline(InlineFormSetFactory):
#     model = FilesDocuments
#     fields = '__all__'
#     # fields = ['id', 'kynd', 'file_document']
#     # extra = 1
#     factory_kwargs = {'extra': 2, 'max_num': None,
#                       'can_order': False, 'can_delete': False}
#     formset_kwargs = {'auto_id': 'my_id_%s'}
#
#
# class ContactInline(InlineFormSetFactory):
#     model = Contact
#     fields = '__all__'
#     # fields = ['description', 'contact']
#     # extra = 1
#     factory_kwargs = {'extra': 1, 'max_num': None,
#                       'can_order': False, 'can_delete': False}
#     formset_kwargs = {'auto_id': 'my_id_%s'}
#
#
# class CreatePerson(CreateWithInlinesView, LayoutMixin):
#     model = Person
#     inlines = [ContactInline, FilesDocumentsInline]
#
#     fields = ['name', 'phone', 'cpf_cnpj', 'email', 'nascimento', 'rg', 'cep', 'logradouro', 'numero', 'bairro',
#               'cidade', 'estado']
#
#     layout = Layout(
#         Fieldset('Pessoa',
#                  Row(Span9('name'), Span3('nascimento'), ),
#                  Row(Span4('phone'), Span4('cpf_cnpj'), Span4('rg')),
#                  Row(Span12('email'), ),
#                  ),
#         Fieldset('Endereço',
#                  Row(Span2('cep'), Span8('logradouro'), Span2('numero')),
#                  Row(Span5('bairro'), Span5('cidade'), Span2('estado')),
#                  # Inline('Qualificações da Profissão', ContactInline),
#                  # Inline('Qualificações da Profissão', FilesDocumentsInline),
#                  ),
#
#     )
#
#     template_name = 'person_create_contact.html'


class PersonFormView(SuccessMessageMixin, FormView):
    form_class = PersonForm
    template_name = 'person_create_contact.html'
    success_url = reverse_lazy('person:person_client_list')
    success_message = 'The person was created correctly.'

    def get_context_data(self, **kwargs):
        context = super(PersonFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['contact_formset'] = ContactForm(self.request.POST, prefix='contacts')
            context['file_formset'] = FileDocumentFormSet(self.request.POST, self.request.FILES, prefix='files')
        else:
            context['contact_formset'] = ContactForm(prefix='contacts')
            context['file_formset'] = FileDocumentFormSet(prefix='files')
        print('-----------------CONTEXT------------------')
        print(context)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        contact_formset = context['contact_formset']
        file_formset = context['file_formset']
        total = 0
        if contact_formset.is_valid() and file_formset.is_valid():
            person = form.save(commit=False)
            person.save()

            contact_formset.instance = person
            contact_formset.save()

            file_formset.instance = person
            file_formset.save()
            # for item_form in contact_formset.forms:
            #     item = item_form.save(commit=False)
            #     item.person = person
            #     item.save()
            #     total += item.quantity * item.unit_price
            # person.total = total
            # person.save()
            return super(PersonFormView, self).form_valid(form)
        else:
            print('-----------------FORM INVALIDO------------------')
            print(file_formset)
            return self.render_to_response(self.get_context_data(form=form))
        
        
def person_create(request, ):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        contact_formset = ContactFormSet(request.POST)

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
    print(str(file_document_formset))
    context = {'form': form,
               'contact_formset': contact_formset,
               'file_document_formset': file_document_formset,
               'forms': forms}
    # from django.template.loader import render_to_string
    # context2 = render_to_string('person_create_contact.html', {'file_document_formset': file_document_formset})
    # print(context2)
    return render(request, 'person_create_contact.html', context)


def person_update(request, id):
    # Pega a chave da URL acima com (request, pk)
    # joga na variável person na linha abaixo passando o modelo MESTRE e os parâmetros que desejo como filtro
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
        print(str(file_document_formset))
        # curl 'person_create_contact.html'

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