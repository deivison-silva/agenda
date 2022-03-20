from django.shortcuts import render
from .models import Contato, Categoria
# Create your views here.


def index(request):
    contatos = Contato.objects.order_by('-data_criacao').all()

    dados = {
        'contatos': contatos
    }

    return render(request, 'contatos/index.html', dados)
