# Generated by Django 4.0.3 on 2022-03-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_contato_descricao_alter_contato_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostar',
            field=models.BooleanField(default=True),
        ),
    ]
