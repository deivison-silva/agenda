# Generated by Django 4.0.3 on 2022-03-24 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_rename_mostar_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
