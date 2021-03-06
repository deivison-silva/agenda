# Generated by Django 4.0.3 on 2022-03-20 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('descricao', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.categoria')),
            ],
        ),
    ]
