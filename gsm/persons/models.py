# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField('Nome',max_length=100)
    birthday = models.DateField('Aniversário')
    observation = models.CharField('Observações',max_length=100)
    purchase_limit = models.DecimalField('Limite de compra',max_digits=15, decimal_places=2)


    class Meta:
        verbose_name_plural = 'pessoas 2'
        verbose_name = 'pessoa 2'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/cadastro/pessoas'


class Address(models.Model):
    KINDS = (
        ('P', 'PRINCIPAL'),
        ('C', 'COBRANÇA'),
        ('E', 'ENTREGA'),
    )
    person = models.ForeignKey('persons.Person', related_name='addresses', on_delete=models.CASCADE)
    kind = models.CharField('Tipo', max_length=1, choices=KINDS)
    public_place = models.CharField('Logradouro',max_length=150)
    number = models.CharField('Número',max_length=150)
    city = models.CharField('Cidade',max_length=150)
    state = models.CharField('Estado',max_length=150)
    zipcode = models.CharField('Cep',max_length=10)
    country = models.CharField('País',max_length=150)
    neighborhood = models.CharField('Bairro',max_length=50)

    class Meta:
        verbose_name_plural = 'endereços'
        verbose_name = 'endereço'
        unique_together = ('person', 'kind')

    def __str__(self):
        return self.public_place


class Client(Person):
    compra_sempre = models.BooleanField('Compra Sempre',default=False)

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('persons:clients_editar', args=[str(self.id)])

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Employee(Person):
    ctps = models.CharField('Carteira de Trabalho',max_length=25)
    salary = models.DecimalField('Salário',max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        # self.operacao = CONTA_OPERACAO_DEBITO
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
# --------------------------------------------------------------------------------------------------------------------


class Customer(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.IntegerField('Total')

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    def get_absolute_url(self):
        return reverse('invoicing:invoice_detail', args=(self.pk,))


KIND_DOCUMENT = (
    ('0', 'RG'),
    ('1', 'CPF'),
    ('2', 'CNH'),
    ('3', 'Comprovante Endereço'),
)


class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    kind = models.TextField('Tipo Documento', max_length=1, choices=KIND_DOCUMENT)
    file_document = models.FileField(upload_to='documents/')
    title = models.CharField('title', max_length=255)
    quantity = models.DecimalField('quantity', max_digits=10, decimal_places=3, default=1)
    unit_price = models.DecimalField('unit price', max_digits=10, decimal_places=2)

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
