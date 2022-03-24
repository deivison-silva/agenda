from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.contrib import messages
from django.http import Http404
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

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
                             'O campo de pesquisa não pode ficar em branco')
        return redirect('contatos')

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
