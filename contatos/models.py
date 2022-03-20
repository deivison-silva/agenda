import email
from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
