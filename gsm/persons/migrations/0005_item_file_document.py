# Generated by Django 2.2 on 2019-11-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_item_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='file_document',
            field=models.FileField(default='documents/23191007348584000130592300765300000143993521-can-sign.xml', upload_to='documents/'),
            preserve_default=False,
        ),
    ]
