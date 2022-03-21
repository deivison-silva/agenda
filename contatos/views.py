from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contato
# Create your views here.


def contatos(request):
    contatos = Contato.objects.order_by('-data_criacao').all()
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
