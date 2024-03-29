# Generated by Django 2.2 on 2019-11-02 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20190718_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('quantity', models.DecimalField(decimal_places=3, default=1, max_digits=10, verbose_name='quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='unit price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Invoice')),
            ],
        ),
    ]
