from django.shortcuts import render, get_object_or_404, redirect #import o error
from django.http import Http404  # Importa o error
from .models import Contato     # Importar as classes que ta no modelss
from django.core.paginator import Paginator    ## Quando for fazer paginação importa o Paginator
from django.db.models import Q, Value           # importa o campo de pesquisa
from django.db.models.functions import Concat    # importa o campo de pesquisa
from django.contrib import messages             # importa a mensagem que aparece no navegador


def index(request):   ## Aq coloca o filtro do id aula 172    
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 10)  ## Coloca o tanto de item vai aparecer por pagina 
    page = request.GET.get('p')         ## Coloca no html aq ficou no indexxxx
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    }) ###  Vai adicionar a classe contatos


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    }) ###  Vai adicionar a classe contatos


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR, 
            'Campo busca não pode ficar vazio'
        )
        return redirect('index')
    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 10)  ## Coloca o tanto de item vai aparecer por pagina 
    page = request.GET.get('p')         ## Coloca no html aq ficou no indexxxx
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    }) ###  Vai adicionar a classe contatos
