from django.db import models

# Create your models here.
from django.urls import reverse

KIND_CONTACT = (
    ('0', 'Telefone Fixo'),
    ('1', 'Celular 1'),
    ('2', 'Celular 2'),
    ('3', 'Celular 3'),
    ('4', 'E-Mail'),
    ('5', 'Telefone Trabalho'),
)

KIND_DOCUMENT = (
    ('0', 'RG'),
    ('1', 'CPF'),
    ('2', 'CNH'),
    ('3', 'Comprovante Endereço'),
)


class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    phone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, null=True, blank=True)
    rg = models.CharField('RG', max_length=18, null=True, blank=True)
    nascimento = models.DateField('Data Nascimento')
    email = models.EmailField('E-Mail', max_length=50, null=True, blank=False)
    cep = models.CharField('Cep', max_length=10, null=True, blank=False)
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.CharField('Número', max_length=10, null=False, blank=False)
    bairro = models.CharField('Bairro', max_length=50, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=50, null=False, blank=False)
    estado = models.CharField('Estado', max_length=10, null=False, blank=False)
    priority = models.PositiveIntegerField('Prioridade', default=0)
    created_on = models.DateField(
        'Criado em.',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        ordering = ('created_on',)
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.email = self.email.lower()
        self.logradouro = self.logradouro.upper()
        self.bairro = self.bairro.upper()
        self.cidade = self.cidade.upper()
        self.estado = self.estado.upper()

        super(Person, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('person: person_update', args=[str(self.id)])

    def __str__(self):
        return self.name


class Contact(models.Model):
    person = models.ForeignKey("person.person",
                               null=False,
                               blank=False,
                               related_name="person_contacts",
                               on_delete=models.CASCADE,
                               verbose_name="Pessoa")
    kind = models.TextField('Tipo Contato', max_length=1, choices=KIND_CONTACT)
    description = models.CharField('Conteúdo', max_length=50, null=True, blank=True)
    contact = models.CharField('Pessoa Contato', max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('kind',)
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def save(self, *args, **kwargs):
        self.description = self.description.upper()
        self.contact = self.contact.upper()

        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.kind


class FilesDocuments(models.Model):
    person = models.ForeignKey("person.person",
                               null=False,
                               blank=False,
                               related_name="person_documents",
                               on_delete=models.CASCADE,
                               verbose_name="Pessoa")
    kind = models.TextField('Tipo Documento', max_length=1, choices=KIND_DOCUMENT)
    file_document = models.FileField(upload_to='documents/')

    class Meta:
        ordering = ('kind',)
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def delete(self, *args, **kwargs):
        self.file_document.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.kind


