# Generated by Django 2.2 on 2019-07-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20190718_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesdocuments',
            name='kind',
            field=models.TextField(choices=[('0', 'RG'), ('1', 'CPF'), ('2', 'CNH'), ('3', 'Comprovante Endereço')], max_length=1, verbose_name='Tipo Documento'),
        ),
    ]
