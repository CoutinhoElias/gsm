from django import forms
from django.forms import inlineformset_factory, formset_factory
from material import Layout, Fieldset, Span3, Row, Span12, Span9, Span4, Span2, Span8, Span5

from gsm.person.models import Person, Contact, FilesDocuments

KIND_CONTACT = (
    ('0', 'Telefone Fixo'),
    ('1', 'Celular 1'),
    ('2', 'Celular 2'),
    ('3', 'Celular 3'),
    ('4', 'E-Mail'),
    ('5', 'Telefone Trabalho'),
)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'name',
            'phone',
            'cpf_cnpj',
            'email',
            'nascimento',
            'rg',
            'cep',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
        )
        exclude = ('priority',)

    layout = Layout(
        Fieldset('Pessoa',
                 Row(Span9('name'), Span3('nascimento'), ),
                 Row(Span4('phone'), Span4('cpf_cnpj'), Span4('rg')),
                 Row(Span12('email'), ),
                 ),
        Fieldset('Endereço',
                 Row(Span2('cep'), Span8('logradouro'), Span2('numero')),
                 Row(Span5('bairro'), Span5('cidade'), Span2('estado'))
                 )
        )


class FileForm(forms.ModelForm):

    class Meta:
        model = FilesDocuments
        # fields = ('kind', 'file_document')
        exclude = ['id']


# widgets={'description': forms.TextInput(attrs={'class': 'input-field'}), },
ContactForm = inlineformset_factory(Person, Contact,
                                    exclude=('id',),
                                    can_delete=True,
                                    fields=('kind', 'description', 'contact'),
                                    extra=0,
                                    min_num=1)

# widgets={'description': forms.FileInput(attrs={'class': 'input-field'}), },
FileDocumentFormSet = inlineformset_factory(Person, FilesDocuments,
                                             exclude=('id',),
                                             can_delete=True,
                                             fields=('kind', 'file_document'),
                                             extra=0,
                                             min_num=1)

FileDocumentFormSet0 = formset_factory(FileForm,
                                      min_num=1,
                                      validate_min=True,
                                      extra=0,
                                      max_num=16,
                                      validate_max=True)

