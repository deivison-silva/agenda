from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato
# Create your views here.


def contatos(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    paginator = Paginator(contatos, 10)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    dados = {
        'contatos': contatos
    }

    return render(request, 'contatos/contatos.html', dados)


def contato(request, id):
    contato = get_object_or_404(Contato, id=id)

    if not contato.mostrar:
        raise Http404()

    dados = {
        'contato': contato
    }

    return render(request, 'contatos/contato.html', dados)


def pesquisa(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')
    
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) |
        Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 10)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    dados = {
        'contatos': contatos
    }

    return render(request, 'contatos/pesquisa.html', dados)
