# Generated by Django 2.2 on 2019-10-23 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0004_auto_20190719_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField()),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('valor_titulo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Titulo')),
                ('operacao', models.CharField(blank=True, choices=[('d', 'Debito'), ('c', 'Credito')], default='d', max_length=1)),
                ('status', models.CharField(blank=True, choices=[('a', 'Aberta'), ('p', 'Paga')], default='a', max_length=1)),
                ('descricao', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('-data_vencimento', 'valor_titulo'),
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('operacao', models.CharField(blank=True, choices=[('d', 'Debito'), ('c', 'Credito')], default='d', max_length=1)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField()),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=15)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conta_pagamento', to='financial.Conta')),
            ],
            options={
                'verbose_name': 'Venda Detalhe',
                'verbose_name_plural': 'Vendas Detalhe',
            },
        ),
        migrations.AddField(
            model_name='conta',
            name='historico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_conta', to='financial.Historico'),
        ),
        migrations.AddField(
            model_name='conta',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_conta', to='person.Person'),
        ),
    ]
