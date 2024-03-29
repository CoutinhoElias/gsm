# Generated by Django 2.2 on 2019-07-01 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=18, null=True, verbose_name='CPF/CNPJ')),
                ('rg', models.CharField(blank=True, max_length=18, null=True, verbose_name='RG')),
                ('nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='E-Mail')),
                ('cep', models.CharField(max_length=10, null=True, verbose_name='Cep')),
                ('logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=10, verbose_name='Estado')),
                ('priority', models.PositiveIntegerField(default=0, verbose_name='Prioridade')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Criado em.')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ('created_on',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.TextField(choices=[('0', 'Telefone Fixo'), ('1', 'Celular 1'), ('2', 'Celular 2'), ('3', 'Celular 3'), ('4', 'E-Mail'), ('5', 'Telefone Trabalho')], max_length=1, verbose_name='Tipo Contato')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Conteúdo')),
                ('contact', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pessoa Contato')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='person.Person', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'ordering': ('kind',),
            },
        ),
    ]
