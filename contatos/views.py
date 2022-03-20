from django.shortcuts import render, get_object_or_404
from .models import Contato
# Create your views here.


def contatos(request):
    contatos = Contato.objects.order_by('-data_criacao').all()

    dados = {
        'contatos': contatos
    }

    return render(request, 'contatos/contatos.html', dados)


def contato(request, id):
    contato = get_object_or_404(Contato, id=id)

    dados = {
        'contato': contato
    }

    return render(request, 'contatos/contato.html', dados)
